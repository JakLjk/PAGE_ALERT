from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

from page_alert.config.common_config import DBConfig, FlaskConfig


db = SQLAlchemy()
DB_NAMEPATH = DBConfig.db_namepath
SECRET_KEY = FlaskConfig.secret_key

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_NAMEPATH
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .webhooks import webhooks


    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(webhooks, url_prefix="/load")

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.sign_in'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists(DB_NAMEPATH):
        with app.app_context():
            db.create_all()
        print('Created Database!')

