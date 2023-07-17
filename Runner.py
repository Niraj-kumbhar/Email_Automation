from scripts.prechecks import prechecks
from scripts.email_main import email_main
from datetime import datetime as dt
import time

dt_format = "%d/%m/%Y %H:%M:%S" # time format

# welcome banner
banner_ = """
             _                                   _ _ 
            | |                                 (_) |
  __ _ _   _| |_ ___         ___ _ __ ___   __ _ _| |
 / _` | | | | __/ _ \       / _ \ '_ ` _ \ / _` | | |
| (_| | |_| | || (_) |  _  |  __/ | | | | | (_| | | |
 \__,_|\__,_|\__\___/  (_)  \___|_| |_| |_|\__,_|_|_|
                                                                                     
"""

print(banner_)
print("Running Prechecks...\n\n")
time.sleep(0.5)

Slog =  open('logs/Scriptlogs.txt','a')
Slog.write(f"\n\n{dt.now().strftime(dt_format)}-->Started, In Runner\n")
Slog.close()

pre = prechecks(1)
pre.data()
pre.error_check()
pre.check_duplicates()
emailPass = pre.security_config()
err = pre.error # getting error flag

Slog =  open('logs/Scriptlogs.txt','a')
Slog.write(f"\n{dt.now().strftime(dt_format)}-->Prechecks completed\n")
print("--"*10,"Prechecks completed","---"*10,"\n\n")

if err == 1:
    Slog.write(f"\n{dt.now().strftime(dt_format)}-->Error flag True")
    opt = input("Above are some errors expected while sending mail, Do you still want to continue(y/n):")
    if opt=="" or opt=='n':
        Slog.write(f"\n{dt.now().strftime(dt_format)}-->User opt out, Exiting Script\n")
        Slog.close()
        print("\n\n.....Exiting")
        exit()
Slog.close()  

print("sending mails .....")
mail = email_main(emailPass[0],emailPass[1])
mail.read_config()
# mail.security_config()
mail.send_mail()
mail.summary()