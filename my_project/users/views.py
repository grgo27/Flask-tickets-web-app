from flask import render_template, redirect, url_for, Blueprint, flash,request
from flask_login import login_user, logout_user, login_required,current_user
from my_project import db   
from my_project.models import User
from my_project.users.forms import RegistrationForm, LoginForm

users=Blueprint('users',__name__)

@users.route('/register',methods=['GET','POST'])
def register():

    form=RegistrationForm()

    if form.validate_on_submit():
        user=User(email=form.email.data,username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('User registered successfully')
        return redirect(url_for('users.login'))
    
    return render_template('register.html',form=form)

@users.route('/login',methods=['GET','POST'])
def login():

    form=LoginForm()

    if form.validate_on_submit():

        user=User.query.filter_by(email=form.email.data).first()
        
        if user is not None and user.check_password(password=form.password.data):
            login_user(user)
            flash('User logged in successfully')

            next=request.args.get('next')

            if next==None or not next[0]=='/':
                next=url_for('core.index')
            
            return redirect(next)
    return render_template('login.html',form=form)

@users.route('/logout')
@login_required
def logout():
    logout_user()
    flash('User logged out sucessfully')
    return redirect(url_for('core.index'))


