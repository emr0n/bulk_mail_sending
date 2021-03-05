import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

list1 = []

with open("mail.txt","r",encoding="utf-8") as file: #This your mails.txt
    content = file.readlines()
    for i in content:
        line = i
        line = line.strip()
        line = line.strip("\n")
        list1.append(line.split((",")))

for i,j in list1:
    message = MIMEMultipart()

    message["From"] = "your_mail_adress@mail.com" #Sender mail adress
    message["To"] = j #Receiver mail adress
    message["Subject"] = "Hello " + i

    text = """
    This is a test mail.
    SMTP MAIL TEST
    """

    message_text = MIMEText(text,"plain")
    message.attach(message_text)

    try:
        mail = smtplib.SMTP("smtp.gmail.com",587) #You can arrange this place for yourself.
        mail.ehlo() # For connect server
        mail.starttls() # For encrypt mail
        mail.login("your_mail_adress@mail.com","your_password") #This your mail and password
        mail.sendmail(message["From"],message["To"],message.as_string())
        print("Mail has been sent successfully!")
        mail.close()
    except:
        sys.stderr.write("There is a problem!")
        sys.stderr.flush()