#!/usr/bin/python3
''' Execute all backup jobs in jobs list.

Usage: python backupooall.py
'''

# import modules

import sys
from emailconfig import EmailConfig
from job import Job
from backup import Backup, BackupFile, BackupDirectory
from backupcfg import job_msg, usage_msg, logfile, email_config, jobs

def main():
    '''
    Execute all backup jobs in job list.
    '''

    # interate through all jobs in jobs list
    for job in jobs:
        
        # Set job attributes

        # determine the type of backup to perform based upon job type
        backup = BackupFile() if job.is_file_job else BackupDirectory() 
        job.set_backup(backup)
           
        job.set_logfile(logfile)
        job.set_email_config(email_config)
            
        # perform backup
        if not job.errors:
            job.do_backup()

        # send errors as email
        if job.errors:
            pass # job.do_email()

        # record result in logfile
            job.do_logfile()
            
    sys.exit(0)

if __name__ == '__main__':
    main()

