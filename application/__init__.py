from flask import Flask, g
from application.model import Session

blueprints = ['server']

def create_app():
    app = Flask(__name__)
    for name in blueprints:
        app.register_blueprint(load_blueprint(name))
    @app.before_request
    def define_session():
        g.session = Session()
    return app

def load_blueprint(name):
    blueprint = getattr(__import__('application.'+name, None, None, ['app']), 'app')
    return blueprint
