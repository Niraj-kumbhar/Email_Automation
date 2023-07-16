import pandas as pd
import os
from html.parser import HTMLParser
from datetime import datetime as dt
  

class prechecks:

    def __init__(self,i=0):
        """initializes the object and sets up the log file for script logging. 
    
        Args:
            i (int, optional): _optional and can be used to prevent the class from running certain checks automatically. Defaults to 0.
        """
        try:
            if i==1: # passing arg to avoid auto run
                #os.chdir('scripts/')
                self.dt_format = "%d/%m/%Y %H:%M:%S"
                Slog =  open('logs/Scriptlogs.txt','a')
                Slog.write(f"\n{dt.now().strftime(self.dt_format)}-->In Prechecks")
                with open('logs/reports.txt','w') as f:
                    f.write("="*10+"Prechecks Report"+"="*10+"\n")
                    f.write(f"DateTime: {dt.now().strftime(self.dt_format)}\n")
                
                self.error = 0
                                

        except Exception as e:
            Slog.write(f"\n\n{dt.now().strftime(self.dt_format)}-->Exception occured\n")
            print(e)

        finally:
            Slog.close()

    def security_config(self):
        """reads the security configuration from the "security.txt" file and retrieves the sender's email and app passcode (password).

        Returns:
            tuple: values read from security.txt
        """
        try:
            Slog =  open('logs/Scriptlogs.txt','a')    
            Slog.write(f"\n{dt.now().strftime(self.dt_format)}-->Reading security config")
            security = {}
            with open('security/security.txt','r') as f:
                for line in f:
                    line = line.strip()
                    name, var=line.partition("=")[::2]
                    security[name.strip()] = str(var).strip()
            # set security
            sender = security['Sender_email'] # change if sender file name is different
            pass_key = security['AppPasscode']
            return (sender, pass_key)
            
        except Exception as e:
            print(e)

    # gathering data
    def data(self):
        """reads the recipient email data and email configuration from files. It stores the data in the DataFrame df and configurations in the dictionary config
        """
        try:
            Slog =  open('logs/Scriptlogs.txt','a') # logs tracking
            Slog.write(f"\n{dt.now().strftime(self.dt_format)}-->reading email_data file")
            self.df = pd.read_csv('email_config/email_data.csv')
            self.config = {}
            with open('email_config/config.txt','r') as f:
                for line in f:
                    line = line.strip()
                    name, var=line.partition("=")[::2]
                    self.config[name.strip()] = str(var).strip()
            Slog.write(f"\n{dt.now().strftime(self.dt_format)}-->reading email_data file completed")
        
        except Exception as e:
            print("Error in prechecks - data reading")
            Slog.write(f"\n{dt.now().strftime(self.dt_format)}--> Error Occured {e}")

        finally:
            Slog.close()
    
         
    def error_check(self):
        """checks for errors related to the presence of files in the "data" directory and the existence of a common file (if required). 
        It logs the results in the "reports.txt" file and sets the error flag to 1 if any errors are found.
        """
        try:
            Slog =  open('logs/Scriptlogs.txt','a') # logs tracking
            Slog.write(f"\n{dt.now().strftime(self.dt_format)}--> checking for errors..")
            for i in range(self.df.shape[0]):
                file = f"{self.df.Name[i]}.{self.config['file_extension']}"
                isExist = os.path.exists(f'data/{file}')
                self.df.loc[i,['isExist']] = isExist
        
            temp = "no"
            with open('logs/reports.txt','a') as f:
                f.write('\n'+'='*10+"File logs"+"="*10+"\n")
                f.write(f"File extension selected: {self.config['file_extension']}\n")
            if self.config['Do you want to send one common file for all email(y/n)'] == 'y':
                isExist_con = os.path.exists(f"data/{self.config['that_common_filename']}.{self.config['file_extension']}")
                temp = f"yes, {self.config['that_common_filename']} will be common file"

                with open('logs/reports.txt','a') as f:
                    f.write(f"Do you want to send one common file for all email(y/n): {temp}\n")

                if isExist_con == False:
                    Slog.write(f"\n{dt.now().strftime(self.dt_format)}--> No common file exists")
                    self.error = 1 # set Error flag true
                    with open('logs/reports.txt','a') as f:
                        f.write(f"data/{self.config['that_common_filename']} not exists\n")

            
            ErrNo = self.df.shape[0] - self.df.isExist.sum()
            list_error = self.df[self.df.isExist==False]['Name'].values.tolist()
            
            
            with open('logs/reports.txt','a') as f:

                f.write(f"No of Files not found : {ErrNo}\n")
                if ErrNo>0:
                    self.error=1 # set Error flag true
                    f.write("\nFile(s) not found for below Names:\n")
                    for i,_ in enumerate(list_error):
                        f.write(f"{i+1}.{_}\n")
            
            #self.check_duplicates()
            Slog.write(f"\n{dt.now().strftime(self.dt_format)}--> checking for errors completed")
            with open('logs/reports.txt','r') as f:
                print(f.read())
        
        except Exception as e:
            print("Error occured prechecks - error_check")
            Slog.write(f"\n{dt.now().strftime(self.dt_format)}--> Error Occured {e}")
        
        finally:
            Slog.close()
    
    def check_duplicates(self):
        """checks for duplicate names and email addresses in the DataFrame df. 
        It logs the duplicate data (if found) in the "reports.txt" file and sets the error flag to 1 if any duplicates are found.
        """
        try:
            Slog =  open('logs/Scriptlogs.txt','a') # logs tracking
            Slog.write(f"\n{dt.now().strftime(self.dt_format)}--> checking for duplicates..")
            dup_name = self.df[self.df.Name.duplicated()]
          
            dup_email = self.df[self.df.Email.duplicated()]

            


            with open('logs/reports.txt','a') as f:
                f.write('\n'+'='*10+"Check Duplicates"+"="*10+"\n")

                f.write(f"Duplicate in Name: {dup_name.shape[0]}\n")
                f.write(f"Duplicate in Emails: {dup_email.shape[0]}\n")

                if dup_name.shape[0]>0:
                    self.error=1 # set Error flag true
                    f.write("\nDuplicate Name Data:\n")
                    Slog.write(f"\n{dt.now().strftime(self.dt_format)}--> Duplicates name found")
                    for _ in dup_name.index:
                        name = dup_name.Name[_]
                        email = dup_name.Email[_]
                        f.write(f"{name} {email}\n")

                if dup_email.shape[0]>0:
                    self.error=1 # set Error flag true
                    f.write("\nDuplicate Email Data:\n")
                    Slog.write(f"\n{dt.now().strftime(self.dt_format)}--> Duplicates email found")
                    for _ in dup_email.index:
                        name = dup_email.Name[_]
                        email = dup_email.Email[_]
                        f.write(f"{name} {email}")
            
        

        except Exception as e:
            print(e)
        finally:
            Slog.close()