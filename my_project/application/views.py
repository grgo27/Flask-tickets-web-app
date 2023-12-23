from flask import render_template, redirect, url_for, Blueprint, flash,request,abort
from flask_login import login_user, logout_user, login_required,current_user
from my_project import db   
from my_project.models import User,TicketApplication
from my_project.application.forms import ApplicationForTicketForm 

apply_tickets=Blueprint('apply_tickets',__name__)

@apply_tickets.route('/apply',methods=['GET','POST'])
@login_required
def apply():
    if current_user.tickets_application: # if current user have application
        abort(400)

    form=ApplicationForTicketForm()

    if form.validate_on_submit():

        apply=TicketApplication(name=form.name.data,
                                surname=form.surname.data,
                                date_of_birth=form.date_of_birth.data,
                                country=form.country.data,
                                city=form.city.data,
                                address=form.address.data,
                                email=form.email.data,
                                number_of_tickets=form.number_of_tickets.data,
                                user_id=current_user.id)
        db.session.add(apply)
        db.session.commit()
        flash('Your application for tickets was succesfull')
        return redirect(url_for('core.index'))
    return render_template('apply.html',form=form)

@apply_tickets.route('/apply_check')
@login_required
def apply_check():
    if current_user.tickets_application: # ako logirani user ima napravljenu aplikaciju za karte
        your_application = TicketApplication.query.get_or_404(current_user.tickets_application.id)
    else:
        abort(406)

    return render_template('apply_check.html',your_application=your_application)

@apply_tickets.route('/update/<int:application_id>',methods=['GET','POST'])
@login_required
def update(application_id):
    
    your_application=TicketApplication.query.get_or_404(application_id)

    form=ApplicationForTicketForm()

    if form.validate_on_submit():
        your_application.name=form.name.data
        your_application.surname=form.surname.data
        your_application.date_of_birth=form.date_of_birth.data
        your_application.country=form.country.data
        your_application.city=form.city.data
        your_application.address=form.address.data
        your_application.email=form.email.data
        your_application.number_of_tickets=form.number_of_tickets.data            

        db.session.commit()
        flash('Application updated')
        return redirect (url_for('apply_tickets.apply_check'))
        
    elif request.method=='GET':
        form.name.data=your_application.name
        form.surname.data=your_application.surname
        form.date_of_birth.data=your_application.date_of_birth
        form.country.data=your_application.country
        form.city.data=your_application.city
        form.address.data=your_application.address
        form.email.data=your_application.email
        form.number_of_tickets.data=your_application.number_of_tickets
        
    return render_template('apply.html',form=form)       
    
@apply_tickets.route('/delete/<int:application_id>',methods=['GET','POST'])
@login_required
def delete(application_id):
    your_application=TicketApplication.query.get_or_404(application_id)
    db.session.delete(your_application)
    db.session.commit()

    return redirect (url_for('core.index'))
