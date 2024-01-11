#!/usr/bin/python3
""" A module that compress web_static file into an archive"""

from fabric.api import local
from datetime import datetime


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
