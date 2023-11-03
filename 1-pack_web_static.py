#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static folder
of an AirBnB Clone repository using the function do_pack.
"""

from fabric import task
from datetime import datetime
import os

@task
def do_pack(c):
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    try:
        # Create the versions directory if it doesn't exist
        os.makedirs("versions", exist_ok=True)

        # Get the current date and time
        date = datetime.now().strftime("%Y%m%d%H%M%S")

        # Define the archive filename
        filename = "versions/web_static_{}.tgz".format(date)

        # Create the .tgz archive using tar
        c.local("tar -cvzf {} web_static".format(filename))

        # Return the archive path if successful
        if os.path.exists(filename):
            return filename
        else:
            return None

    except Exception as e:
        return None

if __name__ == "__main__":
    from fabric.main import program
    program.run()

