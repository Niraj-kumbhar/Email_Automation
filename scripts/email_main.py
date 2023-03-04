from email.mime.application import MIMEApplication
from email.policy import default
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
from datetime import datetime

class email_main:
    

    def __init__(self):
        self.__read_config()
        
        
    
    def __read_config(self):
        # read email_configs
        self.config = {}
        print("config start")
        with open('..//email_config/config.txt','r') as f:
            for line in f:
                line = line.strip()
                name, var=line.partition("=")[::2]
                self.config[name.strip()] = str(var).strip()

        print ('done read')

        self.file_exten = self.config['file_extension'] # file extension

        self.isConstant = True if self.config['Do you want to send one common file for all email(y/n)'] == 'y' else False # is constant file there
        self.constant_att = self.config['that_common_filename'] #if any constant attachment is there for all mails
        self.subject = self.config['Email_Subject'] # set subject
        self.body = open('..//email_config/body.txt','r').read() #change body
        print (' done body')
        # read Receiptents emails
        #Slog.write(f"{datetime.now()}-->Reading email data file\n")

        self.df = pd.read_csv('..//email_config/email_data.csv') # change if recieptent data file name is different
        self.range_ = self.df.shape[0]
        print ("config end")
        print (self.range_)

        self.__security_config()

        
    def __security_config(self):
        print ("security start")
        self.security = {}
        with open('..//security/security.txt','r') as f:
            for line in f:
                line = line.strip()
                name, var=line.partition("=")[::2]
                self.security[name.strip()] = str(var).strip()
        # set security
        self.sender = self.security['Sender_email'] # change if sender file name is different
        self.pass_key = self.security['AppPasscode']

        print ("security end")
        print (self.sender)
        print (self.pass_key)

        #self.__send_mail()

    
    def __send_mail(self):
        # s = smtplib.SMTP('smtp.gmail.com', 587)
        # s.starttls()
        # s.login(self.sender, self.pass_key)

        # for i in range(self.range_):
            

        
        

    def __attachment_file(self,filename):
        # open the file to be sent
       
        

    
        


a = email_main()