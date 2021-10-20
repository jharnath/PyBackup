# PyBackup
# Lachlan 



Document for use of backup 

### program Requirements
* A machine with python 3.4or higher.
* python requests library installed 
* Administrative privilegeson the device. (Able to read/write all source locations)  
* Access to all potential Directories where the program can write a log file.

### how to configure the script
* 1-open the zip and extract to preferable location for use.
* 2-Configure the backup config.py .Ensure that paths for logs are correct.Ensure api enpoint for email is correct. 
* 3-Run script from command line and ensure that the script is working as intendedOpen a terminal window, Powershell ectInput: python3backup.py backupjob1


Set up script to run as a cronjob how to run the script manually 
Open the ZIP folder sent to you previously. 
Right click the Primary program “Newcode.py” Select run as administratorhow to run the script from a cronjob In order •
Open python terminal Terminal;•Write crontab -eto create crontab;
•Press ito launch edit mode;•Write the schedule command 
```
018 * * */usr/bin/python /path/to/file/<FILENAME>.pybackupjob1

```
•Press escto exit edit mode;
•Write :wqto write your crontabany troubleshooting adviceEnsure you have adequate permissions assigned to the user or the script.Ensure correct version of python is running on device, along with the requests library Ensure that email and log configurations are co
