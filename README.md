Welcome to the Python-Notes wiki!

Here are some python programming notes I made when dealing with some interesting situations in programming.

Enjoy!

#### Email
1. Package: smtplib
2. References:
    * [Using Python to Send Email](http://www.pythonforbeginners.com/code-snippets-source-code/using-python-to-send-email)
    * [Python Email Examples](https://docs.python.org/2/library/email-examples.html)

#### SFTP Service
1. Package: pysftp
2. References:
    * [Pysftp homepage](https://pypi.python.org/pypi/pysftp)
    * [Pysftp documentation](http://pysftp.readthedocs.org/en/release_0.2.8/)

#### Exception Handling
1. [Python Handling Exception](https://wiki.python.org/moin/HandlingExceptions)
2. Example:
```python
(x,y) = (5,0)
try:
   z=x/y
except ZeroDivisionError:
   print "divide by zero"
```

#### Task Scheduling
1. Package/Tool: crontab
2. References:
   *  [Cron Wikipedia](https://en.wikipedia.org/wiki/Cron)
   *  [Crontab Quick-Reference](http://www.adminschoice.com/crontab-quick-reference)
2. Example:
```
minute(0-59) hour(0-23) day(1-31) month(1-12) weekday(0-6) command
```

#### MD5 Check
1. Package/Tool: md5sum or hashlib.md5()
2. References:
   * [Generating a MD5 for file in Python](http://stackoverflow.com/questions/3431825/generating-a-md5-checksum-of-a-file)
3. Example:
   * md5sum:
   ``` bash
   md5sum file
   ```
   * hashlib.md5():
   ``` python
   hashlib.md5(open(file,'r').read()).hexdigest() 
   ```

#### PGP Encrption/Decryption
1. Package/Tool: gnupg
2. References:
   * [GnuPG Homepage](https://www.gnupg.org/)
   * [GnuPG Documentation](https://www.gnupg.org/documentation/manuals/gnupg/)
   * [Best Guide to PGP On Linux](https://www.deepdotweb.com/2015/02/17/basic-guide-pgp-linux/)
