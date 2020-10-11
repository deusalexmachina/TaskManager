"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""

import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


taskid = 1
userid = 1


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables"""
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def fetch_tasks():
    """
    A function to returns all tasks in the data store.
    """
    return {"Task1": 1, "Task2": 2, "Task3": 3}


def create_task(name,optional_priority):
    """
    A function to create a task.
    """
    return taskid


def update_task(taskid):
    """
    A function to update the task based on task ID.
    """
    return taskid


def delete_task(taskid):
    """
    A function to delete the task based on task ID.
    """
    return taskid


def fetch_users():
    """
    A function to returns all users in the data store.
    """
    return {"User1": 1, "User2": 2, "User3": 3}


def create_user(name):
    """
    A function to create a user.
    """
    return userid


def update_userDetails(userid):
    """
    A function to update the user based on user ID.
    """
    return userid


def delete_user(userid):
    """
    A function to delete the user based on user ID.
    """
    return userid
