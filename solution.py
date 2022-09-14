from socket import *
import sys
def smtp_client(port=1025, mailserver='127.0.0.1'):
    # Message Contents
    heloCommand = 'HELO Alice\r\n'  
    fromEmail = 'Alice@email.com'
    toEmail = 'bob@crepes.com'
    msg = "\r\n My message"

    mailServerAndPort = (mailserver, port)
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailServerAndPort)
    recv1 = clientSocket.recv(1024)
    recv1 = recv1.decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    if recv1[:3] != '220':
        sys.exit()

    # Send HELO command and print server response.
    clientSocket.send(heloCommand.encode())
    recv3 = clientSocket.recv(1024)
    recv3 = recv3.decode()
    if recv3[:3] != '250':
        sys.exit()

    # Send MAIL FROM command and handle server response.
    fromAddress = f"MAIL FROM:<{fromEmail}>\r\n"
    clientSocket.send(fromAddress.encode()) 
    recv5 = clientSocket.recv(1024)
    recv5 = recv5.decode()
    if recv5[:3] != '250':
        sys.exit()

    # Send RCPT TO command and handle server response.
    rcptAddress = f"RCPT TO:<{toEmail}>\r\n"
    clientSocket.send(rcptAddress.encode()) 
    recv7= clientSocket.recv(1024)
    recv7 = recv7.decode()
    if recv7[:3] != '250':
        sys.exit()
    
    # Send DATA command and handle server response.
    dataMessage = "DATA\r\n"
    clientSocket.send(dataMessage.encode()) 
    recv9 = clientSocket.recv(1024)
    recv9 = recv9.decode()
    if recv9[:3] != '354':
        sys.exit()

    # Send message data.
    clientSocket.send(msg.encode()) 

    # Message ends with a single period, send message end and handle server response.
    endmsg = "\r\n.\r\n"
    clientSocket.send(endmsg.encode())
    recv11= clientSocket.recv(1024)
    recv11 = recv11.decode()
    if recv11[:3] != '250':
        sys.exit()

    # Send QUIT command and handle server response.
    quitMessage = 'QUIT\r\n'
    clientSocket.send(quitMessage.encode())
    recv13 = clientSocket.recv(1024)
    recv13 = recv13.decode()
    if recv13[:3] != '221':
        sys.exit()
    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')