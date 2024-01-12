#!/usr/bin/python3
""" A module that compress web_static file into an archive"""

from fabric.api import local, run, put, env, cd, task
from datetime import datetime
import os

env.hosts = ['54.175.61.3', '34.207.253.213']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """ a Fabric script that generates a .tgz archive from
    the contents of the web_static """

    current_time = datetime.now()
    archive_name = f'web_static_{current_time.strftime("%Y%m%d%H%M%S")}.tgz'

    # make dir
    local('mkdir -p versions')

    # create archive
    result = local(
            f'tar -cvzf versions/{archive_name} web_static', capture=True
            )

    if (result.return_code == 0):
        return f"version/{archive_name}"
    else:
        return None

@task
def do_deploy(archive_path):
    """ Deploy archive!"""

    if not archive_path:
        return False

    # get pathname
    filename = os.path.basename(archive_path)

    # get filename without extension
    name, extension = filename.split('.')

    # get pathname
    filename = os.path.basename(archive_path)

    # Upload archive to remote server
    r1 = put(archive_path, '/tmp/')

    # extract file on the server
    r2 = run(f'mkdir -p /data/web_static/releases/{name}')
    target_folder = f'/data/web_static/releases/{name}'

    r3 = run(f'tar -xzf /tmp/{filename} -C {target_folder}')

    r4 = run(f'rm -f /tmp/{filename}')
    r5 = run(f'cp -r {target_folder}/web_static/* {target_folder}')
    r6 = run(f'rm -rf {target_folder}/web_static')
    r7 = run('rm -rf /data/web_static/current')

    r8 = run(f'ln -s {target_folder} /data/web_static/current')

    results = [r1, r2, r3, r4, r5, r6, r7, r8]

    for result in results:
        if result.failed:
            return False

    return True
