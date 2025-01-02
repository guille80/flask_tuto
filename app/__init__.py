from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
db = SQLAlchemy()

# app/__init__.py

def create_app(settings_module):
    print(f"Creating app {settings_module}")
    app = Flask(__name__, instance_relative_config=True)
    # Load the config file specified by the APP environment variable
    app.config.from_object(settings_module)
    print(app.config)
    # Load the configuration from the instance folder
    if app.config.get('TESTING', False):
        app.config.from_pyfile('config-testing.py', silent=True)
    else:
        app.config.from_pyfile('config.py', silent=True)
    print(app.config)

    print(app.config.get('APP_ENV'))
    print(app.config.get('DEBUG'))

    login_manager.init_app(app)
    login_manager.login_view = "login"

#     ...
# def create_app():
#     app = Flask(__name__)
#
#     app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe-gbr'
#     # app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Qwerty123@localhost:5432/miniblog'
#     # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Qwerty123@172.29.128.1:5432/miniblog'
#     # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:testing@localhost:5432/miniblog'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
#     login_manager.init_app(app)
#     login_manager.login_view = "auth.login"

    db.init_app(app)

    # Registro de los Blueprints
    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    from .admin import admin_bp
    app.register_blueprint(admin_bp)

    from .public import public_bp
    app.register_blueprint(public_bp)

    # Custom error handlers
    register_error_handlers(app)

    return app


def register_error_handlers(app):

    @app.errorhandler(500)
    def base_error_handler(e):
        return render_template('500.html'), 500

    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template('404.html'), 404