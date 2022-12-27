import pandas as pd
import os
from html.parser import HTMLParser
from datetime import datetime

class HTMLFilter(HTMLParser):
    text = ""
    def handle_data(self, data):
        self.text += data

# gathering data
df = pd.read_csv('..//email_config/email_data.csv')
config = {}
with open('..//email_config/config.txt','r') as f:
    for line in f:
        line = line.strip()
        name, var=line.partition("=")[::2]
        config[name.strip()] = str(var).strip()



# def display_mail():
#     html = HTMLFilter()
#     body = open('email_config/body.txt','r').read()
#     html.feed(body)
#     print('='*10,'Email Content','='*10)
#     print(f"Subject: {config['Email_Subject']}")
#     print(html.text)

def error_check():
    print('Checking  ...')
    for i in range(df.shape[0]):
        file = f"{df.Name[i]}.{config['file_extension']}"
        isExist = os.path.exists(f'..//data/{file}')
        df.loc[i,['isExist']] = isExist
   # print("="*10,"Files Not Found","="*10)
    temp = "no"
    with open('..//logs/reports.txt','a') as f:
        f.write('\n'+'='*10+"File logs"+"="*10+"\n")
        f.write(f"File extension selected: {config['file_extension']}\n")
    if config['Do you want to send one common file for all email(y/n)'] == 'y':
        isExist_con = os.path.exists(f"..//data/{config['that_common_filename']}.{config['file_extension']}")
        temp = f"yes, {config['that_common_filename']} will be common file"

        with open('..//logs/reports.txt','a') as f:
            f.write(f"Do you want to send one common file for all email(y/n): {temp}\n")

        if isExist_con == False:
            # print(f"data/{config['that_common_filename']} not exists")
            # print("="*20)
            with open('..//logs/reports.txt','a') as f:
                f.write(f"..//data/{config['that_common_filename']} not exists\n")



    ErrNo = df.shape[0] - df.isExist.sum()
    list_error = df[df.isExist==False]['Name'].values.tolist()
    #print("No of Files not found : ",ErrNo)

    with open('..//logs/reports.txt','a') as f:

        f.write(f"No of Files not found : {ErrNo}\n")
        if ErrNo>0:
            f.write("\nFile(s) not found for below Names:\n")
            for i,_ in enumerate(list_error):
                f.write(f"{i+1}.{_}\n")

def check_duplicates():
    dup_name = df[df.Name.duplicated()]
    dup_email = df[df.Email.duplicated()]

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

with open('..//logs/reports.txt','w') as f:
    f.write("="*10+"Prechecks Report"+"="*10+"\n")
    f.write(f"DateTime: {datetime.now()}\n")

#display_mail()
error_check()
check_duplicates()
with open('..//logs/reports.txt','r') as f:
    print(f.read())

# create mail config function to dislplay mail sub, sender id connection test?