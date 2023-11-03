#!/usr/bin/env python
from datetime import datetime
from fabric.api import env, run, put
import os

# env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with your server IPs
# env.user = '<your_ssh_user>'  # Replace with your SSH username

def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = os.path.basename(archive_path)
        archive_no_extension = os.path.splitext(archive_name)[0]

        # Upload the archive to the /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Create the release directory
        run('mkdir -p /data/web_static/releases/{}'.format(archive_no_extension))

        # Uncompress the archive to the release directory
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(archive_name, archive_no_extension))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(archive_name))

        # Delete the current symbolic link
        run('rm /data/web_static/current')

        # Create a new symbolic link to the new version
        run('ln -s /data/web_static/releases/{} /data/web_static/current'.format(archive_no_extension))

        return True

    except Exception as e:
        return False
