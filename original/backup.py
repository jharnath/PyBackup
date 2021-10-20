  1 #!/usr/bin/python3
  2 
  3 # import modules
  4 import sys, os, pathlib, shutil, smtplib
  5 from datetime import datetime
  6 from backupcfg import jobs, logfile, usage_msg, job_msg, recipient, email_user, email_pwd, server, port
  7 
  8 # declare empty variables to hold messages and error count 
  9 message = []
 10 errors  = 0
 11 
 12 # get current time and convert to formatted string
 13 now = datetime.now()
 14 datestring = now.strftime("%Y%m%d-%H%M%S")
 15 
 16 ##############
 17 # functions
 18 ##############
 19 
 20 def do_logfile(job):
 21 
 22     global datestring
 23     global errors
 24     global message
 25 
 26     file = open(logfile,"a")
 27     for msg in message:
 28         logmsg = datestring + " " + job + " " + msg
 29         file.write(logmsg + "\n")
 30     file.close()
 31 
 32 
 33 def do_backup(job):
 34 
 35     global message
 36     global errors
 37 
 38     # get source and destination file paths
 39     src = jobs[job][0]
 40     dst = jobs[job][1]
 41 
 42     if not os.path.exists(src):
 43         message.append(src + " does not exist FAIL")
 44         errors += 1
 45 
 46     if not os.path.exists(dst):
 47         message.append(dst + " does not exist FAIL")
 48         errors += 1
 49 
 50     if errors == 0:
 51 
 52         p = pathlib.Path(src)
 54         is_a_dir = p.is_dir()
 55 
 56         path = pathlib.PurePath(src)
 57         dstpath = dst + "/" + path.name + "-" + datestring
 58 
 59         if is_a_file == True:
 60             try:
 61                 shutil.copy2(src, dstpath)
 62                 message.append("Backup job " + job + " SUCCESS")
 63             except:
 64                 message.append("Backup job " + job + " FAIL")
 65                 errors += 1
 66 
 67         elif is_a_dir == True:
 68             try:
 69                 shutil.copytree(src, dstpath)
 70                 message.append("Backup job " + job + " SUCCESS")
 71             except:
 72                 message.append("Backup job " + job + " FAIL")
 73                 errors += 1
 74 
 75 
 76 def do_email(job):
 77 
 78     global message
 79 
 80     header     = 'To: ' + recipient + '\n' + 'From: ' + email_user + '\n' + 'Subject: Backup Error ' + job + '\n'
 81 
 82     msg        = header + '\n'
 83     for item in message:
 84         msg = msg + item + '\n'
 85     msg = msg + ' \n\n'
 86 
 87     smtpserver = smtplib.SMTP(server, port)
 88     smtpserver.ehlo()
 89     smtpserver.starttls()
 90     smtpserver.login(email_user, email_pwd)
 91     smtpserver.sendmail(email_user, recipient, msg)
 92     smtpserver.quit()
 93 
 94 ##############
 95 # script logic
 96 ##############
 97 
 98 # check that we have two (and only two) command line arguments
 99 # else: display usage message
100 if len(sys.argv) == 2:
101 
102     # get CLI argument #2
103     # this is the name of the job to run
104     job = sys.argv[1]
105 
106     # check if provided job name is a key in the jobs dictionary
107     if job in jobs:
108 
109         do_backup(job)
110 
111         if errors > 0:
112             pass
113             #do_email(job)
114 
115         do_logfile(job)
116 
117     else:
118         print(job_msg)
119 
120 else:
121     print(usage_msg)
