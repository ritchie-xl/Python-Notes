__author__ = 'ritchie'
import pysftp

with pysftp.Connection("localhost", username="ritchie",password="myn19860713") as sftp:
    sftp.cwd("Downloads")
    sftp.put("fail.txt")
    print sftp.pwd
    sftp.get('clean2.py')

