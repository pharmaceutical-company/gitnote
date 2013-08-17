#!/usr/bin/env python
from flask.ext.script import Manager
from application import create_app

app = create_app()
manager = Manager(app)

@manager.command
def run():
    app.run(debug=True, use_reloader=True)

@manager.command
def run_public(port=7000):
    app.run(debug=True, use_reloader=True, host='0.0.0.0', port=int(port))

@manager.command
def init_db():
    from application.model import Base, engine
    Base.metadata.create_all(engine)

@manager.command
def init_db():
    from application.model import Base, engine
    Base.metadata.drop_all(engine)

if __name__ == '__main__':
    manager.run()
