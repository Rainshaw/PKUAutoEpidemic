from __future__ import absolute_import, unicode_literals

from datetime import datetime
import json

import requests
from celery import shared_task
from django.conf import settings
from django.template import loader
from django.urls import reverse
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from .models import Info
from .postform import tianbiao
from PKUAutoEpidemic.celery import TransactionAwareTask, my_send_mail


@shared_task(base=TransactionAwareTask, bind=True)
def send_detail_url_email(self, info_id, domain):
    """发送激活邮件"""
    # 加密用户信息
    serializer = Serializer(settings.SECRET_KEY, expires_in=60 * 60 * 24 * 365)
    info = Info.objects.get(id=info_id)
    user_name, to_email = info.xh, info.email

    token = {'info_id': info_id}
    token = serializer.dumps(token).decode()
    detail_path = reverse('epidemic:info-detail', kwargs={'token': token})
    active_url = 'http://{}{}'.format(domain, detail_path)

    print('-----尝试发送邮件-------')
    subject, from_email, to = '燕园云战疫注册', settings.EMAIL_FROM, [to_email]
    html_content = loader.render_to_string(
        'email/epidemic/detail_view_email.html',               #需要渲染的html模板
                        {
                            'user_name': user_name,
                            'domain': domain,
                            'active_url': active_url
                        }
                   )

    my_send_mail.delay(subject, html_content, from_email, to)


@shared_task
def send_epidemic_result(domain, info_id, result):
    subject = '燕园云战疫运行结果'
    from_email = settings.EMAIL_FROM
    info = Info.objects.get(id=info_id)
    to = info.email
    html = loader.render_to_string(
        'email/epidemic/send_result.html',
        {
            'domain': domain,
            'user_name': info.xh,
            'result': result,
        }
    )
    my_send_mail.delay(subject, html, from_email, [to])


@shared_task
def send_wechat_result(info_id, result):
    info = Info.objects.get(id=info_id)
    if info.is_wechat:
        token = info.serverchan_token
        url = 'https://sc.ftqq.com/{}.send'.format(token)
        post_form = {
            'text': '燕园云战疫运行结果',
            'desp': result,
        }
        try:
            requests.post(url, data=post_form)
        except requests.RequestException as e:
            print(e)


@shared_task
def hack_epidemic(domain, info_id):
    sess = requests.Session()
    info = Info.objects.get(id=info_id)

    post_form = {
        'xh': info.xh,
        'sfhx': info.sfhx,  # 是否回校 (y/n)

        # 回校需填写
        'hxsj': '',  # 回校时间，格式为“20200409 170200” 2020年4月9日17点02分00秒
        'cfdssm': '',  # 出发地省编号
        'cfddjsm': '',  # 出发地市编号
        'cfdxjsm': '',  # 出发地区编号
        'sflsss': '',  # 是否留宿宿舍 (y/n)
        'sfcx': '',  # 是否出校 (y/n)

        # 不在校需填写
        'dqszdxxdz': info.dqszdxxdz,  # 当前所在地详细地址
        'dqszdsm': info.dqszdsm,  # 当前所在地省编号
        'dqszddjsm': info.dqszddjsm,  # 当前所在地市编号
        'dqszdxjsm': info.dqszdxjsm,  # 当前所在地区编号
        'dqszdgbm': '156',


        'jrtw': info.jrtw,  # 今日体温（如'36.8')
        'sfczzz': 'n',  # 是否存在病症
        'jqxdgj': '',  # 行动轨迹
        'qtqksm': '',  # 其他情况说明
        'tbrq': datetime.now().strftime('%Y%m%d'),  # 填报日期，自动生成
        'yqzd': info.yqzd,  # 疫情诊断

        'dwdzxx': info.dwdzxx,  # 定位地址信息
        'dwjd': info.dwjd,  # 定位经度
        'dwwd': info.dwwd,  # 定位纬度
        'sfdrfj': '' if info.dqszdsm != '11' else 'n',
        'chdfj': '',
        'jkm': info.jkm,  # 健康码状态
        'simstoken': '',

        'sfmjqzbl': 'n',  #是否与确诊病例密接，尚未解除观察
        'sfmjmjz': 'n',  #是否与确诊病例密接者密接，尚未解除观察
        'sfxfd': 'n',  # 5月30日（含）以来，是否去过北京市新发地批发市场
        'sfxfd_jr': 'n',  # 共同生活的家人5月30日（含）以来，是否去过北京市新发地批发市场
        'hsjcjg': '',  # 核酸检测结果
        'jjgcsj': '',  # 开始居家健康观察的时间
        'sfzgfxdq': 'n',  # 目前是否居住在中高风险地区
    }
    try:
        result = tianbiao(info.xh, info.pwd, post_form)
    except requests.RequestException as e:
        print(e)
        result = '网络错误，请联系站长！'
    send_epidemic_result.delay(domain, info_id, result)
    send_wechat_result.delay(info_id, result)


@shared_task
def send_epidemic_alert_everyday(domain):
    info_qs = Info.objects.all()
    for info in info_qs:
        hack_epidemic.delay(domain, info.id)

    return 1