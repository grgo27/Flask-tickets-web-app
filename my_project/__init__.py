import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail



#### APPLICATION SETUP ####

app=Flask(__name__)

app.config['SECRET_KEY']='mysecretkey'

#### EMAIL SETUP ####
sender_email='your_email.gmail.com' # put your email address
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = sender_email
app.config['MAIL_PASSWORD'] = 'your_app_password' # here you need to put your app password
mail = Mail(app)

#### DATABASE SETUP ####

basedir=os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

Migrate(app,db)

#### LOGIN CONFIGURATION ####
login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='users.login'


#### IMPORT I REGISTER BLUEPRINTOVA ####
from my_project.core.views import core
from my_project.error_pages.handlers import error_pages
from my_project.users.views import users
from my_project.application.views import apply_tickets


app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
app.register_blueprint(apply_tickets)