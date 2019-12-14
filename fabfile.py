
# fabfile.py
import os, re
from datetime import datetime
from pprint import pprint

# 导入Fabric API:
from fabric.api import *

env.hosts = ['52.81.31.86'] 
env.user = "ubuntu"
env.key_filename = ["~/.ssh/servLink.pem",]
env.roledefs.update({
    'prod': ['ec2-52-81-31-86.cn-north-1.compute.amazonaws.com.cn'],
})


db_user = 'admin'
db_password = 'Vincijy0228865723' # 

#==============

_TAR_FILE = 'dist-www.tar.gz'

# 服务器，临时文件夹
_REMOTE_TMP_TAR = '/tmp/{}'.format(_TAR_FILE)

# 服务器，项目部署文件夹
_REMOTE_BASE_DIR = '/srv/servlink'

    
_nginx = {
    'from': '{}/{}/{}/{}'.format(_REMOTE_BASE_DIR, 'www', 'conf', 'servlink.nginx.conf'),
    'to': '{}/{}'.format('/etc/nginx/conf.d', 'servlink.nginx.conf')
}

_pjoin = os.path.join


def update():
    # 创建新目录:
    with cd('~/app/servlink-frontend'):
        run('git pull')
        # sudo('killall node')
        run('setsid npm run dev')

           


# def _current_path():
#     return os.path.abspath('.')

# def _now():
#     return datetime.now().strftime('%y-%m-%d_%H.%M.%S')

# def init():
#     sudo('mkdir {}'.format(_REMOTE_BASE_DIR))

# def build():
#     """
#         打包命令, window 下可以用git bash 执行 
#     """
#     #包含的文件
#     includes = ['conf', 'dist']
#     #不包含的文件
#     excludes = ['test', '.*', '*.pyc', '*.pyo', "__pycache__", "*/db", '*.mp3']
#     #执行本地的命令
#     # local('rm -f dist/{}'.format(_TAR_FILE))
#     cmd = ['tar', '--dereference', '-czvf', './remote_dist/{}'.format(_TAR_FILE)]
#     cmd.extend(['--exclude={}'.format(ex) for ex in excludes])
#     cmd.extend(includes)
#     local(' '.join(cmd))

# def config():
#     sudo('cat {} > {}'.format(_nginx['from'], _nginx['to']))


# def deploy():

#     newdir = 'www-{}'.format(datetime.now().strftime('%y-%m-%d_%H.%M.%S'))
#     # 删除已有的tar文件:
#     sudo('rm -f {}'.format(_REMOTE_TMP_TAR))
#     # 上传新的tar文件:
#     put('remote_dist/{}'.format(_TAR_FILE), _REMOTE_TMP_TAR)
#     # 创建新目录:
#     with cd(_REMOTE_BASE_DIR):
#         sudo('mkdir {}'.format(newdir))

#     # 将上传的文件解压到新目录:
#     with cd('{}/{}'.format(_REMOTE_BASE_DIR, newdir)):
#         sudo('tar -xzvf {}'.format(_REMOTE_TMP_TAR))

#     # 重置软链接:
#     with cd(_REMOTE_BASE_DIR):
#         sudo('rm -f www')
#         sudo('ln -s {} www'.format(newdir))
#         sudo('chown root:root www')
#         sudo('chown -R root:root {}'.format(newdir))

#    # #重启Python服务和nginx服务器:
#     with settings(warn_only=True):  
#         sudo('nginx -s reload')   




