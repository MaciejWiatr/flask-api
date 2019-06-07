import smtplib
import codecs
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
fullpath = os.path.realpath(__file__)
folder = os.path.dirname(fullpath)


def send_mail(bot_email, bot_password, my_email, name, email):
    # me == my email address
    # you == recipient's email address
    me = my_email
    you = "maciekwiatr17@gmail.com"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Prosba o kontakt"
    msg['From'] = me
    msg['To'] = you

    # Create the body of the message (a plain-text and an HTML version).
    with codecs.open((folder +'/html/email.html'), 'r', 'utf-8') as file:
        html_file = file.read()

    print(html_file)
    html = html_file.replace('*!*', name).replace('+!+', email)

    # Record the MIME types of both parts - text/plain and text/html.
    part2 = MIMEText(html.encode('utf-8'), 'html', 'utf-8')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part2)
    # Send the message via local SMTP server.
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login(bot_email,  bot_password)
    mail.sendmail(bot_email, my_email, msg.as_string())
    mail.quit()


