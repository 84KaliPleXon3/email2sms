#!/usr/bin/python2.7

#-------------------------#
#      Gmail Checker      #
#-------------------------#

# Download gmail library from https://github.com/charlierguo/gmail
# use http://www.thegeekstuff.com/2010/08/sms-using-email/
import gmail
import getpass
import time
from email.mime.text import MIMEText
from subprocess import Popen, PIPE

def sendMail(n):
    msg = MIMEText("Chk mail.")
    msg["From"] = "user@domain"
    msg["To"] = "1234567890@tmomail.net"
    msg["Subject"] = "Unread mail"
    p = Popen(["/usr/sbin/sendmail", "-t"], stdin=PIPE)
    p.communicate(msg.as_string())

username = "user@gmail.com"
password = getpass.getpass("Password: ")
g = gmail.login(username, password)
if g.logged_in: print "Logged in"
prevNum = 0
while 1:
    numEmails = g.inbox().count(unread=True)
    if numEmails > prevNum: sendMail(numEmails)
    prevNum = numEmails
    time.sleep(5)
g.logout()
