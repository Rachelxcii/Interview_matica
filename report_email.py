#!/usr/bin/env python3

import os, sys
import reports
import emails
from datetime import date

# The main part starts on Line 38

def load_data(pathOfData):
    
    # To load the data of the fruits, create allData variable, is a list of lists
    files = os.listdir(pathOfData)
    data, allData = [], []
    
    for file in files:
        with open(pathOfData + file) as f:
            data = f.readlines()
        allData.append(data)
        
    return allData


def process_data(allData):
    
    # To generate a summary with the name and the weight of each type of fruit
    summary = []
    
    for data in allData:
        summary.append('name: {}\nweight: {}\n'.format(data[0], data[1]))
        # data is a list, and store the information of each fruit
        # data[0] stores the name and data[1] stores the weight
    
    return summary


def main(argv):
    
    # These variables can be changed
    
    # Path to load the data
    pathOfData = os.path.expanduser('~') + '/supplier-data/descriptions/'
    
    # PDF variables
    title = 'Processed Update on {}\n'.format(date.today().strftime('%B %d. %Y'))

    # Email variables
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    
    # Path and name where is saved the attached PDF 
    attachment = '/tmp/processed.pdf'

    
    # From this point there is only code
    
    # To load the data and generate the summary
    allData = load_data(pathOfData)
    summary = process_data(allData)

    # Turn this into a PDF report
    body = '<br/><br/>'.join(summary) # double '<br/>' because we need and empty line
    reports.generate_report(attachment, title, body)
    
    # Generate the message and send the email
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)
    
    # Upgrade: A list of contacts could be made to send the report to more pe

if __name__ == "__main__":
    main(sys.argv)
