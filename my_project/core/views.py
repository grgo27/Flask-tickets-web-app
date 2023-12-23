from flask import render_template, redirect,url_for, Blueprint
from my_project import db   
from my_project.models import User,TicketApplication,Winners
import random
from datetime import datetime
from my_project.core.email_handler import send_winner_notification_email


core=Blueprint('core',__name__)


@core.route('/')
def index():

    all_applications=TicketApplication.query.all()
    number_of_applications=len(all_applications)

    return render_template('index.html',number_of_applications=number_of_applications)


@core.route('/winners')
def winners():
    specific_datetime = datetime(year=2023, month=12, day=23, hour=12, minute=50, second=0)      
    current_datetime = datetime.now()
    all_applications=TicketApplication.query.all()
    number_of_applications=len(all_applications)

    if current_datetime>specific_datetime:

        winners=Winners.query.all()
        if len(winners)==0: # ne mogu koristit is None jer ce ovaj query vratit praznu list sta znaci da None nece bit nikada zato stavljan if duljina liste nije 0 
            if len(all_applications) >= 2: # ako se prijavilo dvoje ili vise
                winning_applications = random.sample(all_applications, k=2) # onda izaberi raandom dvoje
            else: # ako se nije dvoje znaci da je jedan ili niko
                winning_applications = all_applications # ako je niko ova doli for petlja se nece moc izvrsit a ako je jedno onda ce se moc     
            
            for winning_application in winning_applications:
                winner=Winners(application_id=winning_application.id)
                db.session.add(winner)
                send_winner_notification_email(winning_application.email)

            db.session.commit()      

        return render_template('winners.html',winners=winners,number_of_applications=number_of_applications)
    else:        
        return render_template('not_yet.html',number_of_applications=number_of_applications,specific_datetime=specific_datetime)