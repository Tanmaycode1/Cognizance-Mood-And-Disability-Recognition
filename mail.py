import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def mail(email):
   sender_email = "examplemsit@gmail.com"
   receiver_email = email
   password = "smwtujbcmobbmbda"

   message = MIMEMultipart("alternative")
   message["Subject"] = "New client Alert"
   message["From"] = sender_email
   message["To"] = receiver_email


   text = """
   Congratulations Your appointment has been booked 
   time : XX:XX am
   date : xx/xx/xxxx
   meet link : http://127.0.0.1:5000/videocall?roomID={}  
""".format(id)


   part1 = MIMEText(text, "plain")

   message.attach(part1)

   context = ssl.create_default_context()
   with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
       server.login(sender_email, password)
       server.sendmail(
           sender_email, receiver_email, message.as_string()
       )
