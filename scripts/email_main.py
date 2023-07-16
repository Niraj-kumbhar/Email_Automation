from email.mime.application import MIMEApplication
from email.policy import default
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from time import time
import pandas as pd
from datetime import datetime as dt
import math

class email_main:
    """
    designed to send emails with attachments to multiple recipients.
    The class uses the smtplib library to establish an SMTP connection to a Gmail server and sends emails with attachments.
    """

    def __init__(self, sender, pass_key):
        """
        designed to send emails with attachments to multiple recipients. 
        The class uses the smtplib library to establish an SMTP connection to a Gmail server and sends emails with attachments.

        Args:
            sender (str): email id of sender
            pass_key (str): pass code generated
        """
        try:
            self.dt_format = "%d/%m/%Y %H:%M:%S"
            self.Slog = open('logs/Scriptlogs.txt','a')
            self.Slog.write(f"\n\n{dt.now().strftime(self.dt_format)}-->In email_main")
            self.sender = sender
            pass_key = pass_key
            self.start = dt.now()
            self.sent_ = 0

            #connection
            self.Slog.write(f"\n{dt.now().strftime(self.dt_format)}-->Initializing Connection")
            self.s = smtplib.SMTP('smtp.gmail.com', 587)
            self.s.starttls()
            self.s.login(sender, pass_key)
            self._logs = []
            
        except Exception as e:
            print(e)
            self.Slog.write(f"\n{dt.now().strftime(self.dt_format)}-->Err: Connection failed, Exiting")
            self.Slog.close()
            print("Error occurred, Exiting..")
            print(f"Total time taken:{dt.now()-self.start}")
            exit()



    # ref : https://stackoverflow.com/questions/3173320/text-progress-bar-in-terminal-with-block-characters/13685020
    def printProgressBar (self,iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
        # Print New Line on Complete
        if iteration == total: 
            print()    
        
    
    def read_config(self):
        """
        reads the email configuration from files (config.txt, body.txt, and email_data.csv).
        It stores the configuration parameters like the subject, body, file extension, etc., and the recipient emails in a DataFrame.
        """
    
        self.config = {}
        self.Slog.write(f"\n{dt.now().strftime(self.dt_format)}-->Reading config")
        with open('email_config/config.txt','r') as f:
            for line in f:
                line = line.strip()
                name, var=line.partition("=")[::2]
                self.config[name.strip()] = str(var).strip()

        self.Slog.write(f"\n{dt.now().strftime(self.dt_format)}-->Completed with Config")

        self.file_exten = self.config['file_extension'] # file extension

        self.isConstant = True if self.config['Do you want to send one common file for all email(y/n)'] == 'y' else False # is constant file there
        self.constant_att = self.config['that_common_filename'] #if any constant attachment is there for all mails
        self.subject = self.config['Email_Subject'] # set subject
        self.body = open('email_config/body.txt','r').read() #change body
        self.Slog.write(f"\n{dt.now().strftime(self.dt_format)}-->Read Body completed")
        # read Receiptents emails
        self.Slog.write(f"\n{dt.now().strftime(self.dt_format)}'-->Reading email data file\n")

        self.df = pd.read_csv('email_config/email_data.csv') # change if recieptent data file name is different
        self.range_ = self.df.shape[0]
        self.Slog.write(f"\n{dt.now().strftime(self.dt_format)}-->Reading email_data file completed")
        

    # deprecated this function
    def security_config(self):
        self.Slog.write(f"\n{dt.now().strftime(self.dt_format)}-->Reading security config")
        self.security = {}
        with open('security/security.txt','r') as f:
            for line in f:
                line = line.strip()
                name, var=line.partition("=")[::2]
                self.security[name.strip()] = str(var).strip()
        # set security
        self.sender = self.security['Sender_email'] # change if sender file name is different
        self.pass_key = self.security['AppPasscode']

        self.Slog.write(f"\n{dt.now().strftime(self.dt_format)}-->Security config completed")


    
    def send_mail(self):
        """
        sends emails to all the recipients.
        It iterates through the DataFrame containing recipient emails and attachments, attaches the files to the email, and sends them using the established SMTP connection.
        """                
        self.Slog.write(f"\n{dt.now().strftime(self.dt_format)}-->Starting to send mails") 

        self.printProgressBar(0, self.range_, prefix = 'Progress:', suffix = 'Complete', length = 50)
        for i in range(self.range_):
            
            try:
                toaddr = self.df.Email[i]
                filename = self.df.Name[i]

                self.__attachment_file(toaddr=toaddr,filename=filename)
                
                text = self.msg.as_string()
                self.s.sendmail(self.sender, toaddr, text)
                self.sent_+=1
                self._logs.append(1)
                
            
            except Exception as e:
                self.Slog.write(f"\n{dt.now().strftime(self.dt_format)}-->Err while sending mail to {self.df.Name[i]} {e}")
                self._logs.append(0)
                
            finally:
                self.printProgressBar(iteration=i + 1, total=self.range_, prefix = 'Progress:', suffix = 'Complete', length = 50)

        _logs_ = pd.DataFrame(list(zip(self.df.Email,self.df.Name,self._logs)),columns=['Email','Name','Status'])
        _logs_.to_csv("logs/logs.csv")
        self.s.quit()
        self.Slog.write(f"\n{dt.now().strftime(self.dt_format)}-->Connection end")
        


    def __read_attachment(self,filename):
        """private method that reads an attachment file based on the given filename.

        Args:
            filename (any type): file to attach

        Returns:
            binary file: binary version of same file
        """
        self.Slog.write(f"\n{dt.now().strftime(self.dt_format)}-->Reading attachment file")
        attachment = open(f'data/{filename}.{self.file_exten}', "rb")
        return attachment


            

        
    def __attachment_file(self, toaddr, filename):
        """private method that attaches the specified file to the email message.

        Args:
            toaddr (str: email): email address of receiver
            filename (file): file to attach
        """
               
        self.msg = MIMEMultipart() 
        self.msg['From'] = self.sender 
        self.msg['To'] =  toaddr
        #fname = df.Name[i].split()[0]   #for future use : extracts recievers name

        self.msg['Subject'] = self.subject
        self.msg.attach(MIMEText(self.body, 'html')) # attach the body with the msg instance

        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')
        attachment = self.__read_attachment(filename)  # add file name
        p.set_payload((attachment).read()) # To change the payload into encoded form
        encoders.encode_base64(p) # encode into base64
        p.add_header('Content-Disposition', f"attachment; filename= {filename}.{self.file_exten}")
        self.msg.attach(p)    # attach the instance 'p' to instance 'msg'

        # attaching constant file
        if self.isConstant:
            p = MIMEBase('application', 'octet-stream')
            cons = open(f'data/{self.constant_att}.{self.file_exten}','rb')
            p.set_payload((cons).read())
            encoders.encode_base64(p) # encode into base64
            p.add_header(f'Content-Disposition', f"attachment; filename= {self.constant_att}.{self.file_exten}")
            self.msg.attach(p)
        
        
    def summary(self):
        """prints a summary of the email-sending process, including the number of emails sent and the total time taken for the process.
        """
        # time taken minutes and seconds
        diff = (dt.now() - self.start).total_seconds()
        min_dt = math.floor(diff/60)
        sec_dt = math.floor(diff%60)

        print("\n-------------------- Summary ------------------------------")
        print(f"Sent {self.sent_} out of {self.range_} mails")
        print(f"Total time taken: {min_dt} minute {sec_dt} seconds")
        self.Slog.write(f"\n{dt.now().strftime(self.dt_format)}-->End, time taken: {min_dt} minute {sec_dt} seconds\n")
        self.Slog.close()