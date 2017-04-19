import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = "kevin.dudeja2015@vit.ac.in"
toaddr = "kevin.dudeja2015@vit.ac.in","kevindudeja97@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr

#Use count and increment
fo = open("count.txt","r")
x = fo.readline()
x = int(x)

x = str(x)
msg['Subject'] = "APPLICATION RESPONSE FOR SUMMER SCHOOL 2017 #"+x

x = int(x)
x = x + 1
x = str(x)
fw = open("count.txt","w")
fw.write(x + "\n")
fo.close()
fw.close()
 
#resume mail script

body = "Hi,\nI applied for the ACM Summer School at IIT Kharagpur and submitted my application before the deadline but haven't gotten a response yet. \n \nBy when can I expect an email regarding my selection in the program? Because I am really interested in attending this program. \n \nThanks. \n(Sent using python script)"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "kool1997")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()