from email.mime.application import MIMEApplication
from email.policy import default
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from time import time
import pandas as pd
from datetime import datetime

class email_main:
    

    def __init__(self):
        self.start = datetime.now()
        self.__read_config()
        
        
    
    def __read_config(self):
        time_ = datetime.now()
        print (time_ - self.start)
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
        time_ = datetime.now()
        print (time_ - self.start)

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
        time_ = datetime.now()
        print (time_ - self.start)

        self.__send_mail()

    
    def __send_mail(self):
        print ("connection satrt")
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(self.sender, self.pass_key)
        print ("connection done")
        time_ = datetime.now()
        print (time_ - self.start)
         
        for self.i in range(self.range_):
            print ("satrt loop ")
            self.__attachment_file()

            print ("starting process of sending mail")
            text = self.msg.as_string()
            s.sendmail(self.sender, self.toaddr, text)
            print ("mail send done")

        s.quit()
        print ("connection cut")
        time_ = datetime.now()
        print (time_ - self.start)


    def __read_attachment(self,filename):
    # open the file to be sent 
        attachment = open(f'..//data/{filename}.{self.file_exten}', "rb")
        return attachment


            

        
    def __attachment_file(self):
        time_ = datetime.now()
        print (time_ - self.start)
        print ("attachment file satrt")

        self.toaddr = self.df.Email[self.i] 
        
        self.msg = MIMEMultipart() 
        self.msg['From'] = self.sender 
        self.msg['To'] =  self.toaddr
        #fname = df.Name[i].split()[0]   #for future use : extracts recievers name

        self.msg['Subject'] = self.subject

        self.msg.attach(MIMEText(self.body, 'html')) # attach the body with the msg instance


        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')

        filename = self.df.Name[self.i]
        attachment = self.__read_attachment(filename)  # add file name
        
        #attach = MIMEApplication(attachment, _subtype="pdf")
        
        p.set_payload((attachment).read()) # To change the payload into encoded form
        encoders.encode_base64(p) # encode into base64
        
        p.add_header('Content-Disposition', f"attachment; filename= {filename}.{self.file_exten}")
        self.msg.attach(p)    # attach the instance 'p' to instance 'msg'

        # attaching constant file
        if self.isConstant:
            p = MIMEBase('application', 'octet-stream')
            cons = open(f'..//data/{self.constant_att}.{self.file_exten}','rb')
            p.set_payload((cons).read())
            encoders.encode_base64(p) # encode into base64
            p.add_header(f'Content-Disposition', f"attachment; filename= {self.constant_att}.{self.file_exten}")
            self.msg.attach(p)
        print ("attachment file is done")
        time_ = datetime.now()
        print (time_ - self.start)


        # open the file to be sent
       
        

    
        


a = email_main()