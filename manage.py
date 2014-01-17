from flask.ext.script import Manager
from lishengchun import app, models

manager = Manager(app)


@manager.command
def run():
    app.run(debug=True)


@manager.command
def syncdb():
    models.db.create_all()


if __name__ == "__main__":
    manager.run()