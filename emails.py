#!/usr/bin/env python3

import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
import os

# Script with 3 functions: generate_email, send_email and generate_error_email

def generate_email(sender, receiver, subject, body, attachment):
       
    #Generate the email and attach all the information
    message = EmailMessage()

    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receiver
    
    #Prepare the attachment and the body
    with open(attachment, 'rb') as at: # very important use 'rb', I explain why this in my github wiki: https://github.com/Rachelxcii/Rachelxcii/wiki/Error-'UnicodeDecodeError':--Attach-a-PDF-in-a-email-(Python-3)
        pdf = at.read()
    message.add_attachment(pdf, maintype='application',
                               subtype='pdf',
                               filename=os.path.basename(attachment))
    
    text_body = MIMEText(body, 'plain') #'plain' =  _subtype='plain', and _subtype is the minor type and defaults to plain.
    message.attach(text_body)
    
    return message


def send_email(message):
    # Send the message via SMTP server
    server = smtplib.SMTP('localhost')
    server.send_message(message)
    server.quit() 

    
def generate_error_email(sender, receiver, subject, body):
    #Generate the error email and attach all the information
    message = EmailMessage()

    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receiver
    message.set_content(body)
    
    return message
