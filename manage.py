from flask.ext.script import Manager
from lishengchun import app, models

manager = Manager(app)


@manager.command
def run():
    from lishengchun import app
    app.run(debug=True)


@manager.command
def syncdb():
    from lishengchun import models
    models.db.create_all()


if __name__ == "__main__":
    manager.run()