  1 # dictionary of job definitions
  2 # key = name of job
  3 # value = list containing source and destination files/directories
  4 
  5 jobs = {
  6     "job1": ['/home/ec2-user/environment/ictnwk409-class/data/dir1','/home/ec2-user/environment/ictnwk409-class/data/dir2'],
  7     "job2": ['/home/ec2-user/environment/ictnwk409-class/data/file1','/home/ec2-user/environment/ictnwk409-class/data/dir2'],
  8     "job3": ['/home/ec2-user/environment/backup/dir5','/home/ec2-user/environment/backup/dir6']
  9 }
 10 
 11 
 12 logfile = '/home/ec2-user/environment/ictnwk409-class/backup.log'
 13 
 14 usage_msg = 'Bruk: python backup.py <job_name>'
 15 
 16 job_msg = 'Spesifisert jobb ukjent'
 17 
 18 recipient  = 'jsmith@example.com'
 19 email_user = 'jsmith@example.com'
 20 email_pwd  = 'xxxxxxxx'
 21 server     = 'mail.example.com'
 22 port       = 587
