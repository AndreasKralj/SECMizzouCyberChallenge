#This code will be used to send emails to the user given a user and message.

import smtplib
import os

#print os.environ['EMAIL_PW']

def SendSSLEmail(email_address, body):
    if not body:
        body = "Specific error message not specified."
        
    if not email_address:
        print "No email address specified, sending to default user"
        body += "\n\nNote: The email address was not specified, so it was sent to the default authority.\n"
        #Set a default email address for the application.
        email = "ankwdf@mail.missouri.edu"
    
    gmail_user = 'MizzouSEC2018@gmail.com'  
    gmail_password = os.environ['EMAIL_PW'] #It's kind of shady to me that you need to put the password in the code, but it works.

    sent_from = gmail_user  
    to = ['ankwdf@mail.missouri.edu']  
    subject = 'System notification'
    #body = "Hey, what's up?\n\n- You"

    email_text = """  
    From: %s  
    To: %s  
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    #Attempt to send the email
    try:  
        server_SSL = smtplib.SMTP_SSL('smtp.gmail.com:465')
        print "Got here!"
        server_SSL.ehlo()
        print "Got here!"
        server_SSL.login(gmail_user, gmail_password)
        print "Got here!"
        server_SSL.sendmail(sent_from, to, email_text)
        server_SSL.close()

        print 'Email sent!'
    except:  
        print 'Something went wrong...'
    return;

print "Successful email sent:"
SendSSLEmail("ankwdf@mail.missouri.edu", "This is a test!")
print "Missing email address:"
SendSSLEmail("", "This is a test!")
print "Missing body of email"
SendSSLEmail("ankwdf@mail.missouri.edu", "")