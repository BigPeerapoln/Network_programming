import poplib
from email.message import EmailMessage

server = "192.168.168.139"
user = "peerapoln"
passwd = "peerapoln1234"

server = poplib.POP3(server)
server.user(user)
server.pass_(passwd)

msgNum = len(server.list()[1])

for i in range(msgNum):
    for msg in server.retr(i+1)[1]:
        print(msg.decode())