#This code will be used to send emails to the user given a user and message.

import smtplib

gmail_user = 'AnfreasKralj@gmail.com'  
gmail_password = 'pw' #It's kind of shady to me that you need to put the password in the code, but it works.

sent_from = gmail_user  
to = ['ankwdf@mail.missouri.edu']  
subject = 'Test email'
body = "Hey, what's up?\n\n- You"

email_text = """\  
From: %s  
To: %s  
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

#Attempt to send the email
try:  
    server = smtplib.SMTP('smtp.gmail.com:587')
    print "Got here!"
    server.ehlo()
    print "Got here!"
    #This is where the error occurs.
    server.starttls()
    print gmail_user
    print gmail_password
    server.login(gmail_user, gmail_password)
    print "Got here!"
    server.sendmail(sent_from, to, email_text)
    server.close()

    print 'Email sent!'
except:  
    print 'Something went wrong...'
