from my_project import db
from my_project import login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User,user_id)


class User(db.Model,UserMixin):

    __tablename__='users'

    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(64),unique=True,index=True)
    username=db.Column(db.String(64),unique=True,index=True)
    password_hash=db.Column(db.String(256))    

    # one to one relationship
    tickets_application=db.relationship('TicketApplication',backref='user',lazy=True,uselist=False)

    def __init__(self,email,username,password):
        self.email=email
        self.username=username
        self.password_hash=generate_password_hash(password)
    
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"ID: {self.id}, Username: {self.username}"

class TicketApplication(db.Model):

    __tablename__='tickets_application'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(64),nullable=False)
    surname=db.Column(db.String(64),nullable=False)
    date_of_birth=db.Column(db.DateTime,nullable=False)
    country=db.Column(db.String(64),nullable=False)
    city=db.Column(db.String(128),nullable=False)
    address=db.Column(db.String(128),nullable=False)    
    email=db.Column(db.String(128),unique=True,nullable=False)
    number_of_tickets=db.Column(db.Integer,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)

    winners=db.relationship('Winners',backref='tick_application',lazy=True, uselist=False)

    def __init__(self,name,surname,date_of_birth,country,city,address,email,number_of_tickets,user_id):
        self.name=name
        self.surname=surname
        self.date_of_birth=date_of_birth
        self.country=country
        self.city=city
        self.address=address
        self.email=email
        self.number_of_tickets=number_of_tickets
        self.user_id=user_id

    def __repr__(self):
        return f"Ticket application id is: {self.id}"

class Winners(db.Model):
    __tablename__='winners'

    id=db.Column(db.Integer,primary_key=True)
    application_id=db.Column(db.Integer,db.ForeignKey('tickets_application.id'))

    def __init__(self,application_id):
        self.application_id=application_id



