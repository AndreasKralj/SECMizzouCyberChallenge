import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

#Next, log in to the server
server.login("AnfreasKralj@gmail.com", "")

#Send the mail
msg = "
Hello!" # The /n separates the message from the headers
server.sendmail("AnfreasKralj@gmail.com", "ankwdf@mail.missouri.edu", msg)
