- I am big football fan so after my appliction for EURO tickets I got an idea of making a simple web application where you need to register, login, create application for winning the tickets. Winners will be post on site and they will be notified on email.
- Application can be run both with docker or manually because all of the requirements are inside project.
- I implemented email sending, so for that purpose in main **init**.py under EMAIL SETUP for sender_email and app.config['MAIL_PASSWORD'] appropiate credentials should be set.
  Because I chose GMAIL for server, appropiate app password should be generated and put under app.config['MAIL_PASSWORD'].
- In my_project/core/views under view for winners ('/winners'), specific_datetime needs to be set. This is where the date and time of the drawing of the lucky winners is entered, and thus their announcement and notification by email.
- Before running flask db init, flsk db migrate and flask db upgrate should be done for creating a database.
