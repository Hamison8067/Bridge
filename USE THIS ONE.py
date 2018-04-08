  #!/usr/bin/python2

import sys
import socket
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from threading import Thread,Lock
from scapy.all import sniff,IP,sendp,srp1,Ether,ARP,get_if_list,get_if_hwaddr
go = True
defuser = 'user@gmail.com'
defpass = 'pass'
while go == True:
    go = False
    user =input("Enter Username:  ")
    if user != defuser:
        go = True
    passw = input("Enter Password:  ")
    if passw != defpass
        go = True

msg = MIMEMultipart()
msg['From'] = user
msg['To'] = user
msg['Subj'] = 'LOGGED IN'
msg.attach(MIMEText('YOU JUST LOGGED IN'))

try:
    mailServer - smtplib.SMTP('smtp.gmail.com', 587)

    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(user, passw)
    mailServer.sendmail(user, user, msg.as_String())
    mailServer.close()
except:
    goto 13

    s = socket.socket(AF_INET, SOCK_STREAM)
    s.bind(socket.gethostbyaddr(), 47808)
    dest = socket.socket(AF_INET, SOCK_STREAM)
while True:

        s.listen(1)
    conn, addr = s.accept()
    data = conn.recv(524)

    dest.connect(192.168.1.168, 47808)
    dest.sendall()


