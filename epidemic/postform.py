import random
from . import iaaa


def login(username, password):
    token, sess = iaaa.login(username, password)
    url = 'https://portal.pku.edu.cn/portal2017/ssoLogin.do?_rand={}&token={}'
    rand = str(random.random())
    url = url.format(rand, token)
    sess.get(url)
    return sess


def epidemic_auth(username, password):
    sess = login(username, password)
    url = 'https://portal.pku.edu.cn/portal2017/util/appSysRedir.do?appId=epidemic'
    sess.get(url)
    return sess


def tianbiao(username, password, post_form):
    sess = epidemic_auth(username, password)
    url = 'https://ssop.pku.edu.cn/stuAffair/edu/pku/stu/sa/jpf/yqfk/stu/saveMrtb.do'
    res = sess.post(url, data=post_form)
    return res.text
