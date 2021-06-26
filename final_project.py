import smtplib
from email.mime.text import MIMEText

s = smtplib.SMTP('smtp.id.xensource.com')
s.set_debuglevel(1)
msg = MIMEmultipart("""body""")
sender =  "kss.shiddiq@example.com"
recipients = "sayyid@gmail.com", "shiddiq@example.com"
msg["Subject"] = "Example"
msg["From"] = sender
msg["To"] = recipients
s.sendmail(sender, recipients.split(","), msg.as_string())