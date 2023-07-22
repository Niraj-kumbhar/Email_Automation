# Auto.Email - Email_Automation
__auto.email__ is a Command-line based tool to send batches of emails with some attachments, attachments can be the same for all or different for each email, it's on you!
#### Things to do Before you start sending:
* Keep your email id and secret app code in the `security/security.txt` file
* Save Email content to `body.txt`, change `config.txt` according to you, and add the receiver's info in `email_data.csv`
* Keep all attachments in the data folder with the name same as a receiver (CASE SENSITIVE)
* Run the below command if there is no error emails will be sent or you will get a prompt for confirmation
  
  		poetry run python Runner.py

* Script will print the time taken at the end, and will generate 2 logs files, `logs.csv` and `Scriptlogs.txt`.

![email](https://github.com/Niraj-kumbhar/Email_Automation/assets/89059809/b441da29-86a0-480b-85e4-817c8c738d8d)

## Download and Setup
* You will need to install [Python 3.11](https://www.python.org/downloads/) and then install [Poetry](https://python-poetry.org/docs/#installation)
* clone this github repo

  		git clone https://github.com/Niraj-kumbhar/Email_Automation.git
  OR you can download this using GUI and then extract the downloaded zip file.
	<img src="https://github.com/Niraj-kumbhar/Email_Automation/assets/89059809/642ac947-6970-4185-8461-eff0a2e90a02" alt="download-instruction" width="550" height="300">

* Go to Command-line and change directory location to email_automation folder, and run the below command so poetry will take care of adding dependencies
  
  		poetry install
  
* It's all good to go now!


# Account Prerequisites:
* Should have Gmail id with 2-step authentication enabled.
* Generate App password for a custom app, copy and save password
* for more information, use this [documentation](https://support.google.com/accounts/answer/185833?hl=en)
> __Note:__ It is important that you have to enable 2-step authentication and use the App password as the password for the script, as Google policy has changed to improve security


# Reference
* https://www.abstractapi.com/guides/sending-email-with-python
* https://www.geeksforgeeks.org/send-mail-attachment-gmail-account-using-python/
* https://stackoverflow.com/questions/31715138/how-to-add-href-link-in-email-content-when-sending-email-through-smtplib
