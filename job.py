#!/usr/bin/python3

#EVERYTHING ON LINE 100 - 1005 NEEDS TO BE MOVED 4 SPACE TO THE RIGHT, HAVE FUN.

# import modules
import json, requests   
import pathlib
import smtplib
import os
from datetime import datetime

class Job(object):
    '''
    Individual job details.
    '''

    def __init__(self, *args):
        '''
        class Job constructor

        Set class attributes to initial values.

        Parameters:
            args[0]: job name
            args[1]: source file or directory
            args[2]: destination directory
        '''

        self.name = args[0]
        self.src = args[1]
        self.dst = args[2]

        self.errors = 0
        self.message = []
        self.datestring = datetime.now().strftime("%Y%m%d-%H%M%S")

        # Determine type of backup job
        self.is_file_job = pathlib.Path(self.src).is_file()
        self.is_dir_job = pathlib.Path(self.src).is_dir()

        # Check job source and destination paths exist
        if not os.path.exists(self.src):
            self.message.append("Source " + self.src + " does not exist -> FAIL")
            self.errors += 1

        if not os.path.exists(self.dst):
            self.message.append("Destination directory " + self.dst + " does not exist -> FAIL")
            self.errors += 1

     def __eq__(self, other):
        '''
        Return:
            True when other is name
        '''

        return other == self.name

     def set_backup(self, backup):
        '''
        Set backup 
        '''
        
        self.backup = backup
        
    def set_email_config(self, email_config):
         '''
        Set email_config
        '''
        
        self.email_config = email_config
        
     def set_logfile(self, logfile):
        '''
        Set logfile
        '''
        
        self.logfile = logfile
    
     def do_logfile(self):
        '''
        Output all log messages to logfile.
        '''

        file = open(self.logfile, "a")
        for msg in self.message:
            logmsg = self.datestring + " " + self.name + " " + msg
            file.write(logmsg + "\n")
        file.close()
                                                                                                                                                           
     def set_emailurl(self, emailurl):
        '''
        Set emailurl
        '''
        
        self.emailurl = emailurl
     
    
     def do_email(self):  
        
                 #global message
   #endpoint = https://endpoint.com/JsonEmail"
    hdrs = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    msg  = "Backup Job: %s \n" % job  
    for item in self.message:
        msg = msg + item + '\n'
    body = json.dumps({'message': msg })
    r = requests.post(self.emailurl, data=body, headers=hdrs)
 
 
 
        '''
    def do_email(self):
        
       # Output all log message as email.
        
        
        header = 'To: ' + self.email_config.recipient + '\n' + 'From: ' + self.email_config.user + '\n' + 'Subject: Backup Error ' + self.name + '\n'
        msg = header + '\n'
        
        for item in self.message:
            msg = msg + item + '\n'
        msg = msg + '\n\n'

        smtpserver = smtplib.SMTP(self.email_config.server, self.email_config.port)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.login(self.email_config.user, self.email_config.pwd)
        smtpserver.sendmail(self.email_config.user, self.email_config.recipient, msg)
        smtpserver.quit()
'''
        
        
      def do_backup(self):
        '''
        Backup file system object to destination.
        '''

        # Construct source and destination paths
        src_path = pathlib.PurePath(self.src)
        dst_path = self.dst + "/" + src_path.name + "-" + self.datestring

        # Copy file system object to destination
        try:
            self.backup.do_backup(self.src, dst_path)
            self.message.append(self.backup.prompt + self.src + " -> SUCCEED")
        except:
            self.message.append(self.backup.prompt + self.src + " -> FAIL")
            self.errors += 1
