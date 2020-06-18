from django.db import models
from db.base import BaseModel
from django.core.validators import RegexValidator


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

    sm_regex = RegexValidator(regex=r'^\d{0,3}$', message="编号格式错误。")
    dqszdsm = models.CharField(validators=[sm_regex], max_length=128, verbose_name='当前所在省编号')
    dqszddjsm = models.CharField(validators=[sm_regex], max_length=128, verbose_name='当前所在市编号')
    dqszdxjsm = models.CharField(validators=[sm_regex], max_length=128, verbose_name='当前所在区/县编号')
    dqszdxxdz = models.CharField(max_length=128, verbose_name='当前所在地详细地址')

    sfmjqzbl = models.CharField(max_length=128, choices=_choices, default='n', verbose_name='是否与确诊病例密接，尚未解除观察')
    sfmjmjz = models.CharField(max_length=128, choices=_choices, default='n', verbose_name='是否与确诊病例密接者密接，尚未解除观察')
    sfxfd = models.CharField(max_length=128, choices=_choices, default='n', verbose_name='5月30日（含）以来，是否去过北京市新发地批发市场')
    sfxfd_jr = models.CharField(max_length=128, choices=_choices, default='n', verbose_name='共同生活的家人5月30日（含）以来，是否去过北京市新发地批发市场')
    sfzgfxdq = models.CharField(max_length=128, choices=_choices, default='n', verbose_name='目前是否居住在中高风险地区')

    jrtw = models.FloatField(default=36.8, verbose_name='今日体温（如\'36.8\')')
    sfczzz = models.CharField(max_length=128, default='n', choices=_no_choices, verbose_name='是否存在病症')

    dwdzxx = models.CharField(max_length=128, verbose_name='定位地址信息')
    dwjd = models.FloatField(verbose_name='定位经度')
    dwwd = models.FloatField(verbose_name='定位纬度')

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

    is_email = models.BooleanField(default=True, verbose_name='通过邮件接收填写反馈')
    email = models.EmailField(verbose_name='邮箱地址')

    is_wechat = models.BooleanField(default=False, verbose_name='通过微信接受反馈结果')
    serverchan_token = models.CharField(max_length=128, blank=True, null=True, verbose_name='ServerChan的Secret Key')

