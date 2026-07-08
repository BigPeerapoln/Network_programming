import smtplib

message = """From: From Joe <peerapoln@ubuntu>
To: To Henry <peerapoln@ubuntu>
MIME-Version: 1.0
Content-type: text/html
Subject: Test HTML Email

This is an email message sent as HTML.

<b>This is a test HTML Message .< /b>
<h1>This is headling 1</h1>
"""
try:
    smtp = smtplib.SMTP("192.168.168.139",25)
    smtp.sendmail("peerapoln@localhost", "peerapoln@localhost", message)
    print("Email sent successfully")
except Exception as err:
    print(str(err))