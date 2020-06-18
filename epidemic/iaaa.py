import requests


def login(username, password):
    sess = requests.session()
    sess.get('https://portal.pku.edu.cn/portal2017/login.jsp')
    sess.get(
        'https://iaaa.pku.edu.cn/iaaa/oauth.jsp?'
        'appID=portal2017&'
        'appName=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6%E6%A0%A1%E5%86%85%E4%BF%A1%E6%81%AF%E9%97%A8%E6%88%B7%E6%96%B0%E7%89%88'
        '&redirectUrl=https://portal.pku.edu.cn/portal2017/ssoLogin.do')
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

    res = requests.post(url=login_url, data=post_form)

    return res.json()['token'], sess
