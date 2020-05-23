import requests
import random
from . import iaaa


def login(username, password):
    token, cookie = iaaa.login(username, password)
    url = 'https://portal.pku.edu.cn/portal2017/ssoLogin.do?_rand={}&token={}'
    rand = str(random.random())
    url = url.format(rand, token)
    # print(url)
    headers = {
        "Host": "portal.pku.edu.cn",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
        "Cookie": cookie,
        "Upgrade-Insecure-Requests": '1',
    }
    session = requests.session()
    session.get(url, headers=headers)
    # print(session.cookies.values()[0])
    # print("\n\n\n\n")
    return session.cookies.values()[0]


def auth(username, password):
    cookie = login(username, password)
    cookie = "JSESSIONID={}; " \
             "portalLanguage=; " \
             "UM_distinctid=1720225d71fcf3-0846430512c9bd-30667d00-1fa400-1720225d720f98; " \
             "_webvpn_key=eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiMTYwMDAxMTM3OCIsImlhdCI6M" \
             "TU4OTc3NTg5NCwiZXhwIjoxNTg5ODYyMjk0fQ.5HGUbLlHb45Jf1pHLNkZbzss9dIpNDJSM6CZh_Icplc; " \
             "webvpn_username=1600011378%7C1589775894%7C" \
             "f4516b1aeb2574bb757acc3798e3c227f979d1f9".format(cookie)
    url = 'https://portal.pku.edu.cn/portal2017/'
    headers = {
        "Host": "portal.pku.edu.cn",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-User": "?1",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
        "Cookie": cookie,
        "Upgrade-Insecure-Requests": '1',
    }

    res = requests.get(url, headers=headers)
    # print("====fetch /portal2017=====")
    # print(str(res.content, encoding='utf-8'))

    url = 'https://portal.pku.edu.cn/portal2017/util/appSysRedir.do?appId=epidemic'
    headers = {
        "Host": "portal.pku.edu.cn",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-User": "?1",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
        "Cookie": cookie,
        "Upgrade-Insecure-Requests": '1',
    }

    res = requests.get(url, headers=headers)
    # print(res.__dict__)
    # print(res.cookies.items())

    url = res.url
    # print(url)
    session = requests.session()
    res = session.get(url)
    # print(session.cookies.items())

    # print(str(res.content, encoding='utf-8'))
    # print(session.cookies.items())
    # print(res.url)
    return session


def tianbiao(username, password, post_form):
    session = auth(username, password)

    url = 'https://ssop.pku.edu.cn/stuAffair/edu/pku/stu/sa/jpf/yqfk/stu/yqfk.jsp'

    res = session.get(url)

    # post_form = {
    #     'xh': '1600011378',
    #     'sfhx': 'n',
    #     'hxsj': '',
    #     'cfdssm': '',
    #     'cfddjsm': '',
    #     'cfdxjsm': '',
    #     'dqszdxxdz': '康瑞小区5-3-401',
    #     'dqszdsm': '13',
    #     'dqszddjsm': '05',
    #     'dqszdxjsm': '30',
    #     'dqszdgbm': '156',
    #     'sfqwhb14': 'n',
    #     'sfjchb14': 'n',
    #     'sfqwjw14': 'n',
    #     'sfjcjw14': 'n',
    #     'sflsss': '',
    #     'jrtw': '37',
    #     'sfczzz': 'n',
    #     'jqxdgj': '',
    #     'qtqksm': '',
    #     'tbrq': '20200522',
    #     'yqzd': '健康',
    #     'sfcx': '',
    #     'dwdzxx': '河北省邢台市新河县新河镇富强街',
    #     'dwjd': '115.23859',
    #     'dwwd': '37.5145',
    #     'sfdrfj': '',
    #     'chdfj': '',
    #     'jkm': '绿码',
    #     'simstoken': '',
    # }

    url = 'https://ssop.pku.edu.cn/stuAffair/edu/pku/stu/sa/jpf/yqfk/stu/saveMrtb.do'
    res = session.post(url, data=post_form)
    print(res.json())
    return res.text
