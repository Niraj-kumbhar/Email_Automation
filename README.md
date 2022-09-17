# Email_Automation
![email_automation](https://user-images.githubusercontent.com/89059809/190844538-dce36821-4fbf-4cde-bd51-4705a51601b7.png)
This script can be useful to send multiple emails with attachment (with different attachment to different person)

# Download and Setup
* Downlaod [Python 3.10.6](https://www.python.org/downloads/release/python-3106/) from Official Python website.
* Download this github script (you can use GUI to download)
* After downloading, Open command prompt and change your folder location using `cd` command (for example I have downloaded script in F:)and then run `pip install` following command to install packages required:

		cd /d F:/email_autoamtion
		pip install -r requirements.txt


# Sender Email Account Prerequisites:
* Should have gmail id with 2 step authentication enabled.
* Generate App password for custom app, copy and save password
* for more information, use this [documentation](https://support.google.com/accounts/answer/185833?hl=en)
> __Note:__ It is important that you have to enable 2 step authentication and use App password as password for script, as Google policy have changed to improve security


 # Files and Folder
 * After Setting up your environment, lets setup files and folders according to our script
 > I will suggest keep names of files and folders as mentioned above, if you change name you need to the script also. 

*  `data` --> Keep your all attachment files in this folder, and file names will be same as name of receiptents.
* `email_config` --> Folder contains files that will use for email contents
	* `body.txt` : Keep your body inside this
	* `config.txt` : It is key value pair file, you can change subject, attachment file extension and comman file name using this.
	* `email_data.csv` store your receiptents Email and Name

*  security --> Folder will have `security.txt` file which will contain sender email address and App Password generated on google.

*  `automated_email_script.py` is main script
*  `requirements.txt` for installing required packages
*  After running script, it will print runtime of script in command line and will generate excel file named `logs.csv`. logs file will have reciever data with status (0 or 1). 
	* 1 --> mail send successfully
	* 0 --> Error mail not sent

# Run Script
* After verifying all things, open command prompt and use following command to start script:

		python automated_email_script.py

* Script will print runtime at the end, and will generate log file.

   

# Reference
* https://www.abstractapi.com/guides/sending-email-with-python
* https://www.geeksforgeeks.org/send-mail-attachment-gmail-account-using-python/
* https://stackoverflow.com/questions/31715138/how-to-add-href-link-in-email-content-when-sending-email-through-smtplib
