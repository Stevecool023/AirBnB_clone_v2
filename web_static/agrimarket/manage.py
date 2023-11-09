#!/usr/bin/env python3

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Initialize Flask-Script
manager = Manager(app)

# Add the Migrate command to the manager
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
