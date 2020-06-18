# PKUAutoEpidemic

这是一个自动填写北京大学燕园云战疫的网站程序。

## 安装
本程序安装环境需要
- MySQL
- RabbitMQ
- Redis
- Python 3.8

本程序的`Python`环境依赖由Pipenv管理，安装Pipenv后进入项目目录，使用命令
```text
pipenv install
```
即可安装依赖包

## 初始化
项目根目录下有两个配置文件
- config.sample.ini
- uwsgi.sample.ini

进行重命名去掉.sample后，修改相应内容即可

## 运行
修改完成后，在项目根目录进入Python虚拟环境，运行命令
```text
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
uwsgi --ini uwsgi.ini
```
即可启动网站，如您拥有域名可自行配置nginx反代
```text
location ^~ 
{
    include uwsgi_params;
    uwsgi_pass 127.0.0.1:10805; #与uwsgi.ini中设置一致
    index  index.html index.htm;
    client_max_body_size          1000m;
    client_body_timeout           5m;
    proxy_connect_timeout         5m;
    proxy_read_timeout            5m;
    proxy_send_timeout            5m;
}

location ^~ /static
{
    alias /path/to/PKUAutoEpidemic/static;
}
```

## 重启或停止
在项目目录下进入python虚拟环境
```text
uwsgi --reload uwsgi.pid //重启
uwsgi --stop uwsgi.pid //停止
```

## 问题相关
有任何问题欢迎提Issue
