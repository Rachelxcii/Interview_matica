#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(filename, title, body):
    
    # Generate a report file, type PDF, filename = path + name
    
    style = getSampleStyleSheet() #load the style
    
    reportFile = SimpleDocTemplate(filename) #create the base document
    
    reportTitle = Paragraph(title, style['h1']) #create the title, with 'h1' letter format
    reportBody = Paragraph(body, style['Normal']) #create the body (text), with normal format
    emptyLine = Spacer(1, 20) #empty line, is always in this way
    
    reportFile.build([reportTitle, emptyLine, reportBody])
