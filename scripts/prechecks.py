import pandas as pd
import os
from html.parser import HTMLParser
from datetime import datetime



class HTMLFilter(HTMLParser):
    print("in html")
    text = ""
    def handle_data(self, data):
        self.text += data
    print("completed html")
    

class prechecks:

    def __init__(self):
        with open('..//logs/reports.txt','w') as f:
         f.write("="*10+"Prechecks Report"+"="*10+"\n")
         f.write(f"DateTime: {datetime.now()}\n")
        print("start")
        self.data()
        print("in prechecks")
        self.error_check()
        print("error check complete")
        self.check_duplicates()
        print("checking for duplicate completed")
        with open('..//logs/reports.txt','r') as f:
          print(f.read())
    
    # gathering data
    def data(self):
        self.df = pd.read_csv('..//email_config/email_data.csv')
        self.config = {}
        with open('..//email_config/config.txt','r') as f:
            for line in f:
                line = line.strip()
                name, var=line.partition("=")[::2]
                self.config[name.strip()] = str(var).strip()
        print("action completed")
    
    
         
    def error_check(self):
        print('Checking  ...')
        for i in range(self.df.shape[0]):
            file = f"{self.df.Name[i]}.{self.config['file_extension']}"
            isExist = os.path.exists(f'..//data/{file}')
            self.df.loc[i,['isExist']] = isExist
    # print("="*10,"Files Not Found","="*10)
        temp = "no"
        with open('..//logs/reports.txt','a') as f:
            f.write('\n'+'='*10+"File logs"+"="*10+"\n")
            f.write(f"File extension selected: {self.config['file_extension']}\n")
        if self.config['Do you want to send one common file for all email(y/n)'] == 'y':
            isExist_con = os.path.exists(f"..//data/{self.config['that_common_filename']}.{self.config['file_extension']}")
            temp = f"yes, {self.config['that_common_filename']} will be common file"

            with open('..//logs/reports.txt','a') as f:
                f.write(f"Do you want to send one common file for all email(y/n): {temp}\n")

            if isExist_con == False:
                # print(f"data/{config['that_common_filename']} not exists")
                # print("="*20)
                with open('..//logs/reports.txt','a') as f:
                    f.write(f"..//data/{self.config['that_common_filename']} not exists\n")



        ErrNo = self.df.shape[0] - self.df.isExist.sum()
        list_error = self.df[self.df.isExist==False]['Name'].values.tolist()
        #print("No of Files not found : ",ErrNo)

        with open('..//logs/reports.txt','a') as f:

            f.write(f"No of Files not found : {ErrNo}\n")
            if ErrNo>0:
                f.write("\nFile(s) not found for below Names:\n")
                for i,_ in enumerate(list_error):
                    f.write(f"{i+1}.{_}\n")
        
    
    def check_duplicates(self):
        dup_name = self.df[self.df.Name.duplicated()]
        print(dup_name)
        dup_email = self.df[self.df.Email.duplicated()]

        # print('Checking duplicates...')
        # print(f'Total Duplicates Found: {dup_name.shape[0]+dup_email.shape[0]}')

        with open('..//logs/reports.txt','a') as f:
            f.write('\n'+'='*10+"Check Duplicates"+"="*10+"\n")
            # f.write(f"Duplicate Rows: {dup_.shape[0]}")
            f.write(f"Duplicate in Name: {dup_name.shape[0]}\n")
            f.write(f"Duplicate in Emails: {dup_email.shape[0]}\n")

            if dup_name.shape[0]>0:
                f.write("\nDuplicate Name Data:\n")
                for _ in dup_name.index:
                    name = dup_name.Name[_]
                    email = dup_name.Email[_]
                    f.write(f"{name} {email}\n")

            if dup_email.shape[0]>0:
                f.write("\nDuplicate Email Data:\n")
                for _ in dup_email.index:
                    name = dup_email.Name[_]
                    email = dup_email.Email[_]
                    f.write(f"{name} {email}")


    



   
p= prechecks()
