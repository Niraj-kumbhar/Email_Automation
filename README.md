# Email_Automation
This script can be useful to send multiple emails with attachment (with different attachment to different person).

# Download and setup
You can use command line to download script or directly download using GUI.
After downloading, Use following command to install packages require <br>
`pip install requirements.txt`

# Sender Email Account Prerequisites:
* Should have gmail id with 2 step authentication enabled.
* Generate App password for custom app, copy and save password
* for more information, use this [documentation](https://support.google.com/accounts/answer/185833?hl=en)
> __Note:__ It is important that you have to enable 2 step authentication and use App password as password for script, as Google policy have changed to improve security


 # How to use
 * Create New folder and save your files and script as shown below structure
   Main folder


    <img src='https://user-images.githubusercontent.com/89059809/189541432-d164db63-e376-464d-bd78-5de0c88fabc5.png'>    

	  *  data --> this folder will contain all files that you have to attach
	  *  security --> this folder will contain 2 files `app_pass.txt` for storing password and `sender_email.txt` for storing email address of sender
	  *	 email_content --> this folder will conatin 2 files `body.txt` for storing body of email and `mail_subject.txt` for storing subject of mail
	  *  `automated_email_script.py` is script where you can change email subject and body
	  *  `email_data.xlsx` store receiptents Email and Name
	  *  `requirements.txt` for installing required packages
	  *  Script will generate `logs.xlsx` file with status for email_sent
	  <br><br>

	  > I will suggest keep names of files and folders as mentioned above, if you change name you need to the script also.


  * Verify that `Name` column in `email_data.xlsx` have same name file in data folder
  * Run script using command line
	  `python automated_email_script.py`
* After running script, it will print runtime of script in command line and will generate excel file named `logs.xlsx`. logs file will have reciever data with status (0 or 1). 
	* 1 --> mail send successfully
	* 0 --> Error mail not sent

   

# Reference
* https://www.abstractapi.com/guides/sending-email-with-python
* https://www.geeksforgeeks.org/send-mail-attachment-gmail-account-using-python/
* https://stackoverflow.com/questions/31715138/how-to-add-href-link-in-email-content-when-sending-email-through-smtplib
