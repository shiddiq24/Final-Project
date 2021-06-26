from socket import 
import ssl
import base64
import time

msg = "\r\n Final Project Basic Python b7-b"
endmsg = "\r\n.\r\n"

mailserver =("smtp.gmail.com", 465)

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket = ssl.wrap_socket(clientSocket, ssl_version = ssl.PROTOCOL_SSLv23)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024)
print(recv)
if recv.decode()[:3] != '200':
    print("220 reply not received from server.")

heloCommand = "HELO Alice\r\n"
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024)
print(recv1)
if recv1.decode([:3]) != '250':
    print("250 reply not received from server.\n")

username = "kss.shiddiq@gmail.com"
password = ""
base64_str = ("\x00" + password).encode()
base64_str = base64.b64encode(base64_str)
authMsg = "AUTH PLAIN".encode() + base64_str + "\r\n".encode()
clientSocket.send(authMsg)
recv_auth = clientSocket.recv(1024)
print(recv_auth.decode())

mailFromCommand = "MAIL FROM: <kss.shiddiq@gmail.com>\r\n"
clientSocket.send(mailFromCommand.encode())
recv2 = clientSocket.recv(1024)
print("After MAIL FROM command: " + recv2.decode())

rcptToCommand = "RCPT To: <shiddiq.alba@gmail.com>\r\n"
clientSocket.send(rcptToCommand.encode())
recv3 = clientSocket.recv(1024)
print("After RCPT TO command: " + recv3.decode())

dataCommand = "DATA\r\n"
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024)
print("After DATA command: " + recv4.decode())

to = "To: <shiddiq.alba@gmail.com>\r\n\r\n"
clientSocket.send(to.encode())

subject = "Subject: Final Project\r\n\r\n"
clientSocket.send(subject.encode())
clientSocket.send(msg.encode())

clientSocket.send(endmsg.encode())
recv6 = clientSocket.recv(1024)
print("Response after sending meesage body: "+ recv6.decode())

quit = "QUIT\r\n"
clientSocket.send(quit.encode())
recv7 = clientSocket.recv(1024)
print(recv7.decode())
clientSocket.close()
