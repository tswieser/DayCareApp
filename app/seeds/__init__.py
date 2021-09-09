from flask.cli import AppGroup
from .users import seed_users, undo_users
from .school import seed_school, undo_school
from .classes import seed_class, undo_class

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_school()
    seed_class()
    seed_users()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_class()
    undo_school()
# Add other undo functions here
