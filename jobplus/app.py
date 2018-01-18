import datetime
from flask import Flask
from jobplus.config import configs
from jobplus.models import db, User, Company
from flask_login import LoginManager 
from flask_migrate import Migrate

def register_extensions(app):
    db.init_app(app)
    Migrate(app, db)
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(id):
        return User.query.get(id)
    login_manager.login_view = 'front.login'

def register_filters(app):

    @app.template_filter()
    def timesince(value):
        now = datetime.datetime.utcnow()
        delta = now - value
        
        if delta.days > 365:
            return '{}year before'.format(delta.days // 356)
        if delta.days > 30:
            return '{}months before'.format(delta.days // 30)
        if delta.seconds > 3600:
            return '{}hours befor'.format(delta.seconds // 3600)
        return 'just now '

def register_blueprints(app):
    from .handlers import front,user, company, job,admin
    app.register_blueprint(front)

    app.register_blueprint(user)
    app.register_blueprint(job)
    app.register_blueprint(company)
    app.register_blueprint(admin)
#    app.register_blueprint(test)



def create_app(config):

    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    
    register_blueprints(app)
    
    db.init_app(app)
    register_extensions(app)
    register_blueprints(app)
    register_filters(app)


    return app

