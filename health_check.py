#!/usr/bin/env python3

import shutil, psutil, socket
import os
import emails
import reports

# Main part starts on Line 34, variables that can be modified from Line 51

def check_cpu_usage():
    #Report an error if CPU usage is over 80%
    usage = psutil.cpu_percent(1)
    return usage < 80


def check_disk_space(disk):
    #Report an error if available disk space is lower than 20%
    diskUsage = shutil.disk_usage(disk)
    freeSpace = diskUsage.free / diskUsage.total * 100
    return freeSpace > 20


def check_memory():
    #Report an error if available memory is less than 500MB
    memoryUsage = psutil.virtualmemory().available/(1024*1024)
    return memoryUsage > 500


def check_localhost():
    #Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
    localhost = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"

# MAIN PART OF THE CODE

errorMessage = ''

# Check something wrong and change the errorMessage
if check_cpu_usage():
    errorMessage = 'CPU usage is over 80%'
elif check_disk_space('/'):
    errorMessage = 'Available disk space is less than 20%'
elif check_memory():
    errorMessage = 'Available memory is less than 500MB'
elif check_localhost():
    errorMessage = 'localhost cannot be resolved to 127.0.0.1'

# If something's wrong, send an errorMessage
if errorMessage != '':
    
    # Can change these variables
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = 'Error - {}'.format(errorMessage)
    body = 'Please check your system and resolve the issue as soon as possible.'
    
    # Generate and send the email
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)
