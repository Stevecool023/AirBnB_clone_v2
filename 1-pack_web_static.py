#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the
the contents of the web_static folder of AirBnB clone repo
using the function do_pack
"""

from fabric import Connection, task
from datetime import datetime
import os

@task
def do_pack(c):
    """The Fabric script to generate a .tgz archive from
    the content of the web_static folder.
    """
    try:
        os.makedirs("versions", exist_ok=True)
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = "versions/web_static_{}.tgz".format(date)
        c.local("tar -cvzf {} web_static".format(filename))
        return filename
    except Exception:
        return None

if __name__ == "__main__":
    from fabric.main import program
    program.run()

