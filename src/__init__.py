from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config['SECRET-KEY'] = 'bin_to_dec'

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app