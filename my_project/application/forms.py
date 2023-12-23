from flask_wtf import FlaskForm
from wtforms import StringField, SelectField,DateField,SubmitField,IntegerField
from wtforms.validators import Email,DataRequired
from wtforms import ValidationError
from datetime import datetime

class ApplicationForTicketForm(FlaskForm):

    name=StringField('Name',validators=[DataRequired()])
    surname=StringField('Surname',validators=[DataRequired()])
    date_of_birth=DateField('Date of birth',validators=[DataRequired()]) # bit ce mali izbornik za izabrat datum, ali datum ce bit u defaultnom formatu yyyy-mm-dd
    country=SelectField(u'Select your country',choices=[('Albania','Albania'),('Austria','Austria'),('Belgium','Belgium'),('Croatia','Croatia'),('Czechia','Czechia'),('Denmark','Denmark'),('England','England'),('France','France'),('Germany','Germany'),('Hungary','Hungary'),('Italy','Italy'),('Netherlands','Netherlands'),('Portugal','Portugal'),('Romania','Romania'),('Scotland','Scotland'),('Serbia','Serbia'),('Slovakia','Slovakia'),('Slovenia','Slovenia'),('Spain','Spain'),('Switzerland','Switzerland'),('Turkiye','Turkiye')],validators=[DataRequired()])
    city=StringField('City',validators=[DataRequired()])
    address=StringField('Address',validators=[DataRequired()])    
    email=StringField('Contact Email',validators=[DataRequired(),Email()])
    number_of_tickets=IntegerField('How many tickets?',validators=[DataRequired()])
    submit=SubmitField('Apply')

    def validate_date_of_birth(self,date_of_birth):
        min_date = datetime.strptime('01.01.1900', '%d.%m.%Y').date() # triba prvo konvertirat u datetime objekt jer nemogu usporedivat datum sa stringon
        max_date = datetime.strptime('20.12.2023', '%d.%m.%Y').date()
        if self.date_of_birth.data < min_date or self.date_of_birth.data > max_date:
            raise ValidationError('Date must be between {} and {}'.format(min_date.strftime('%d.%m.%Y'), max_date.strftime('%d.%m.%Y'))) # ode san stavija da u erroru vrati opet u odgovarajucem obliku
    
    def validate_number_of_tickets(self,number_of_tickets):
        if self.number_of_tickets.data > 4:
            raise ValidationError('You can only apply for 4 tickets or less')