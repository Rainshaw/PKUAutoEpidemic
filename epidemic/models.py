from django.db import models
from db.base import BaseModel
from django.core.validators import RegexValidator

'''
info = {


    'dwdzxx': '',  # 定位地址信息
    'dwjd': '',  # 定位经度
    'dwwd': '',  # 定位纬度
    'sfdrfj': '',
    'chdfj': '',
    'jkm': '绿码',  # 健康码状态
    'simstoken': '',
}
'''


class Info(BaseModel):
    id_regex = RegexValidator(regex=r'^\d{8,12}$', message="账号格式错误。")
    xh = models.CharField(validators=[id_regex], max_length=16, unique=True, verbose_name='学号')

    pwd = models.CharField(max_length=128, verbose_name='密码')

    _choices = (
        ('n', '否'),
        ('y', '是'),
    )
    _no_choices = (
        ('n', '否'),
    )
    _null_choices = (
        ('', '空'),
    )
    sfhx = models.CharField(max_length=128, default='n', choices=_no_choices, verbose_name='是否回校')

    # dqszdgbm = models.CharField(max_length=128, choices=(('156', '中国'),), default='156',
    #                             verbose_name='当前所在国家')
    sm_regex = RegexValidator(regex=r'^\d{0,3}$', message="编号格式错误。")
    dqszdsm = models.CharField(validators=[sm_regex], max_length=128, verbose_name='当前所在省编号')
    dqszddjsm = models.CharField(validators=[sm_regex], max_length=128, verbose_name='当前所在市编号')
    dqszdxjsm = models.CharField(validators=[sm_regex], max_length=128, verbose_name='当前所在区/县编号')
    dqszdxxdz = models.CharField(max_length=128, verbose_name='当前所在地详细地址')

    sfqwhb14 = models.CharField(max_length=128, choices=_choices, default='n', verbose_name='14日内是否途径湖北或前往湖北')
    sfjchb14 = models.CharField(max_length=128, choices=_choices, default='n', verbose_name='14日内是否接触过来自湖北地区的人员')
    sfqwjw14 = models.CharField(max_length=128, choices=_choices, default='n', verbose_name='14日内是否有境外旅居史')
    sfjcjw14 = models.CharField(max_length=128, choices=_choices, default='n', verbose_name='14日内是否接触过境外人员')

    jrtw = models.FloatField(default=36.8, verbose_name='今日体温（如\'36.8\')')
    sfczzz = models.CharField(max_length=128, default='n', choices=_no_choices, verbose_name='是否存在病症')
    # jqxdgj = models.CharField(max_length=128, null=True, blank=True, verbose_name='行动轨迹')
    # qtqksm = models.CharField(max_length=128, null=True, blank=True, verbose_name='其他情况说明')
    # tbrq = datetime.now().strftime('%Y%m%d')# 填报日期，自动生成
    dwdzxx = models.CharField(max_length=128, verbose_name='定位地址信息')
    dwjd = models.FloatField(verbose_name='定位经度')
    dwwd = models.FloatField(verbose_name='定位纬度')
    # sfdrfj = models.CharField(max_length=128, default='', choices=_null_choices, null=True, blank=True,
    #                           verbose_name='是否当日返京')
    # chdfj = models.CharField(max_length=128, default='', choices=_null_choices, null=True, blank=True,
    #                          verbose_name='从何地返京')
    yqzd_choices = (
        ('健康', '健康'),
        ('医学观察', '医学观察'),
        ('疑似', '疑似'),
        ('确诊', '确诊'),
        ('治愈', '治愈'),
        ('解除观察', '解除观察')
    )
    yqzd = models.CharField(max_length=128, choices=yqzd_choices, default='健康', verbose_name='疫情诊断')
    jkm = models.CharField(max_length=128, default='绿码', verbose_name='健康码状态')
    # simstoken = models.CharField(max_length=128, choices=_null_choices, null=True, blank=True,
    #                              verbose_name='未知参数simstoken')
    is_email = models.BooleanField(default=True, verbose_name='通过邮件接收填写反馈')
    email = models.EmailField(verbose_name='邮箱地址')

    is_wechat = models.BooleanField(default=False, verbose_name='通过微信接受反馈结果')
    serverchan_token = models.CharField(max_length=128, blank=True, null=True, verbose_name='ServerChan的Secret Key')

    # hxsj = '',  # 回校时间，格式为“20200409 170200” 2020年4月9日17点02分00秒
    # cfdssm = '',  # 出发地省编号
    # cfddjsm = '',  # 出发地市编号
    # cfdxjsm = '',  # 出发地区编号
    # sflsss = '',  # 是否留宿宿舍 (y/n)
    # sfcx = '',  # 是否出校 (y/n)
