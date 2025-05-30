import smtplib
sender="scarofcupid@gmail.com"
receiver="receiver@gmail.com"
password="useyourownappgeneratedpassword"
message="Hello,This is an example of test mail!! "
try :
 with smtplib.SMTP('smtp.gmail.com',587) as server :
     server.starttls()
     server.login(sender,password)
     server.sendmail(sender,receiver,message)
     print("Message sent !!")
except ConnectionRefusedError:
    print("SMTP isn't installed by default and the connection is refused as a result !!")
