from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Email,EqualTo,DataRequired
from my_project.models import User
from flask_login import current_user
from wtforms import ValidationError

class RegistrationForm(FlaskForm):

    email=StringField('Email',validators=[DataRequired(),Email()])
    username=StringField('Username',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message='Passwords must match!')])
    pass_confirm=PasswordField('Confirm Password',validators=[DataRequired()])
    submit=SubmitField('Register')

    def validate_email(self,email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('That Email has already been registered')
    
    def validate_username(self,username):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('That Username has already been registered')
        

class LoginForm(FlaskForm):

    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Login')


