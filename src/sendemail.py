__author__ = 'Lei Xia'

import smtplib
import pysftp

from email.mime.text import MIMEText

def main():
    #Gmail Login
    username = "lei@hudsondata.com"
    password = "myn19860713"

    #Gmail Server
    server = smtplib.SMTP("smtp.gmail.com:587")

    # Construct the email
    fp = open("fail.txt",'rb')
    msg = MIMEText(fp.read())
    fp.close()

    send_from = 'Monkey Runner'
    send_to = 'lei@hudsondata.com'

    msg['Subject'] = '[Error] Fail to download the bidding data'
    msg['From'] = send_from
    msg['To'] = send_to

    #Add multiple email to the recipients list
    recipients = [send_to, "ritchie_xl@hotmail.com"]

    #Sending the email
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username,password)
    server.sendmail(send_from,recipients, msg.as_string())
    server.quit()


if __name__ == "__main__":
    main()
