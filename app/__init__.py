from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)


    #ORM에 대한 설정
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app,db)


    from .views import basic_views, hyunji_views
    app.register_blueprint(basic_views.fisa)
    app.register_blueprint(hyunji_views.hyunji)
    
    return app