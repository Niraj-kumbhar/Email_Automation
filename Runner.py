from scripts.prechecks import prechecks
from scripts.email_main import email_main
from datetime import datetime as dt

dt_format = "%d/%m/%Y %H:%M:%S" # time format

Slog =  open('logs/Scriptlogs.txt','a')
Slog.write(f"\n\n{dt.now().strftime(dt_format)}-->Started, In Runner\n")
Slog.close()

pre = prechecks(1)
pre.data()
pre.error_check()
pre.check_duplicates()
err = pre.error # getting error flag

Slog =  open('logs/Scriptlogs.txt','a')
Slog.write(f"\n{dt.now().strftime(dt_format)}-->Prechecks completed\n")
print("--"*10,"Prechecks completed","---"*10,"\n\n")

if err == 1:
    Slog.write(f"\n{dt.now().strftime(dt_format)}-->Error flag True\n")
    opt = input("Above are some errors expected while sending mail, Do you still want to continue(y/n):")
    if opt=="" or opt=='n':
        Slog.write(f"\n{dt.now().strftime(dt_format)}-->User opt out, Exiting Script\n")
        print("\n\n.....Exiting")
        exit()
    
print("sending mails .....")