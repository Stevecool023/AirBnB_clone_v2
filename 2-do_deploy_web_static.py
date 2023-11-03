#!/usr/bin/python
"""
A Fabric script that distributes an archive to your web servers, using the function do_deploy.
"""

from fabric.api import env, run, put
from os.path import exists

env.hosts = ['35.153.232.148', '54.234.35.137']
# All remote commands must be executed on both web servers

def do_deploy(archive_path):
    """Distributes an archive to web servers."""
    if exists(archive_path) is False:
        return False  # Returns False if the file at archive_path doesn't exist

    filename = archive_path.split('/')[-1]
    no_extension = filename.split('.')[0]
    release_path = "/data/web_static/releases/{}".format(no_extension)
    current_path = "/data/web_static/current"
    tmp_path = "/tmp/{}".format(filename)

    try:
        put(archive_path, "/tmp/")
        # Upload the archive to the /tmp/ directory of the web server

        run("mkdir -p {}".format(release_path))
        # Uncompress the archive to the folder /data/web_static/releases/
        # <archive filename without extension> on the web server
        run("tar -xzf {} -C {}/".format(tmp_path, release_path))
        run("rm {}".format(tmp_path))

        run("mv {}/web_static/* {}/".format(release_path, release_path))
        run("rm -rf {}/web_static".format(release_path))
        # Delete the archive from the web server

        run("rm -rf {}".format(current_path))
        # Delete the symbolic link /data/web_static/current from the web server

        run("ln -s {} {}".format(release_path, current_path))
        # Create a new symbolic link /data/web_static/current on the
        # web server, linked to the new version of your code
        # (/data/web_static/releases/<archive filename without extension>)

        return True
    except BaseException:
        return False
