"""We will firstly write a unique file for automatically sending email to adresses scrapped in a pdf file"""

# Import Packages
import os
import smtplib
from email.message import EmailMessage
from PyPDF2 import PdfReader
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd

# Parameters
## Define the path of the file
file_path = '/Users/adamelbernoussi/Desktop/Stages_2A_2022-2023.2715202705.pdf'

# Preprocessing 
df = PdfReader(file_path)
#df = pd.DataFrame(df.pages[0].extract_text().split('\n'))
print(df.pages[0].extract_text())

# Define the function

