#!/usr/bin/python
"""
With Fabric, creates a tgz archive
from web_static content folder
"""

from fabric.api import local, put, run, sudo
from os.path import exists, isdir
from datetime import datetime

def do_pack():
    """Creates a tgz archive using Fabric"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        filename = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except Exception as ex:
        return None

def do_deploy(archive_path):
    """Deploy web static with Fabric"""
    if exists(archive_path) is False:
        return False

    try:
        filename = archive_path.split("/")[-1]
        no_extension = filename.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        sudo('mkdir -p {}{}/'.format(path, no_extension))
        sudo('tar -xzf /tmp/{} -C {}{}/'.format(filename, path, no_extension))
        sudo('rm /tmp/{}'.format(filename))
        sudo('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_extension))
        sudo('rm -rf {}{}/web_static'.format(path, no_extension))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {}{}/ /data/web_static/current'.format(path, no_extension))
        return True
    except BaseException:
        return False

def deploy():
    """Do pack and do deploy"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
