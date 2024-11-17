from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"]='65b0b774279de460f1cc5c92'
    app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///ums.sqlite"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config["SESSION_PERMANENT"]=False
    app.config["SESSION_TYPE"]='filesystem'
    from .routes import bp as main_bp
    db.init_app(app)
    bcrypt.init_app(app)
    Session(app)

    app.register_blueprint(main_bp)
    with app.app_context():
        db.create_all()

    return app