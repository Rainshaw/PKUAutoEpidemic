import requests


def get_cookie():
    url = 'https://iaaa.pku.edu.cn/iaaa/oauth.jsp?appID=portal2017&appName=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6%E6%A0%A1%E5%86%85%E4%BF%A1%E6%81%AF%E9%97%A8%E6%88%B7%E6%96%B0%E7%89%88&redirectUrl=https://portal.pku.edu.cn/portal2017/ssoLogin.do'
    res = requests.get(url)
    res = res.cookies.values()
    return res[0]


def login(username, password):
    login_url = 'https://iaaa.pku.edu.cn/iaaa/oauthlogin.do'
    post_form = {
        "userName": username,
        "password": password,
        "appid": 'portal2017',
        "randCode": '',
        "smsCode": '',
        "otpCode": '',
        "redirUrl": "https://portal.pku.edu.cn/portal2017/ssoLogin.do",
    }

    cookie = get_cookie()
    # print("JSESSIONID:\t{}".format(cookie))

    cookie = "UM_distinctid=1720225d71fcf3-0846430512c9bd-30667d00-1fa400-1720225d720f98; " \
             "_webvpn_key=eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiMTYwMDAxMTM3OCIsImlhdCI6MTU4OTc3NTg5NCwiZXhwIjoxNTg5ODYyMjk0fQ.5HGUbLlHb45Jf1pHLNkZbzss9dIpNDJSM6CZh_Icplc;"\
             " webvpn_username=1600011378%7C1589775894%7Cf4516b1aeb2574bb757acc3798e3c227f979d1f9; "\
             "JSESSIONID={}".format(cookie)
    # print("cookie:\t{}".format(cookie))
    headers = {
        "Host": "iaaa.pku.edu.cn",
        "Connection": "keep-alive",
        "Content-Length": "154",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://iaaa.pku.edu.cn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://iaaa.pku.edu.cn/iaaa/oauth.jsp?appID=portal2017&appName=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6%E6%A0%A1%E5%86%85%E4%BF%A1%E6%81%AF%E9%97%A8%E6%88%B7%E6%96%B0%E7%89%88&redirectUrl=https://portal.pku.edu.cn/portal2017/ssoLogin.do",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
        "Cookie": cookie,
    }

    res = requests.post(url=login_url, data=post_form, headers=headers)
    # print(res.json())
    # print("IAAA Finish")
    return res.json()['token'], cookie