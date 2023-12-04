import os
import smtplib

EMAIL_ADRESS = os.environ.get('USER_MAIL')
EMAIL_PASSWORD = os.environ.get('USER_PASS')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)

    subject = 'Grab dinner this weekend ?'
    body = 'How about dinner at 6pm ?'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADRESS, 'johannforever@gmail.com', msg)