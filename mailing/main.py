from fileinput import filename
import smtplib
from email import encoders, message
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP("smtp.gmail.com", 465)

server.ehlo()
# server.login('myemail@gmail.com', 'password')
with open('password.txt', 'r') as f:
    password = f.read()

server.login('myemail@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'Myself'
msg['To'] = 'targetemail@gmail.com'
msg['Subject'] = 'Just a text'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))
filename = 'shoes.jfif'
attachmet = open(filename, 'rb') #rb = read bin

p = MIMEBase('applications', 'octet-stream')
p.set_payload(attachmet.read())

encoders.encode_base64(p)
p.add_header('Content-Dispostion', f'attachment, filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('myemail@gmail.com', 'targetemail@gmail.com', text)

