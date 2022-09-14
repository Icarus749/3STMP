from socket import *
import sys
def smtp_client(port=1025, mailserver='127.0.0.1'):
    # Email Message Contents
    heloCommand = 'HELO Alice\r\n'  
    fromEmail = 'Alice@email.com'
    toEmail = 'bob@crepes.com'
    msg = "\r\n My message"
    # Command Messages
    quitMessage = 'QUIT\r\n'
    resetMessage = "RSET\r\n"
    mailServerAndPort = (mailserver, port)
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailServerAndPort)
    recv1 = clientSocket.recv(1024)

    # Send HELO command and print server response.
    clientSocket.send(heloCommand.encode('ascii'))
    recv3 = clientSocket.recv(1024)

    # Send MAIL FROM command and handle server response.
    fromAddress = f"MAIL FROM:<{fromEmail}>\r\n"
    clientSocket.send(fromAddress.encode('ascii')) 
    recv5 = clientSocket.recv(1024)

    # Send RCPT TO command and handle server response.
    rcptAddress = f"RCPT TO:<{toEmail}>\r\n"
    clientSocket.send(rcptAddress.encode('ascii')) 
    recv7= clientSocket.recv(1024)
    
    # Send DATA command and handle server response.
    dataMessage = "DATA\r\n"
    clientSocket.send(dataMessage.encode('ascii')) 
    recv9 = clientSocket.recv(1024)
    #recv9 = recv9.decode()
    #if recv9[:3] != '354':
    #    clientSocket.send(resetMessage.encode('ascii'))   
    #    clientSocket.send(quitMessage.encode('ascii'))
    #    sys.exit()

    # Send message data.
    clientSocket.send(msg.encode('ascii')) 

    # Message ends with a single period, send message end and handle server response.
    endmsg = "\r\n.\r\n"
    clientSocket.send(endmsg.encode('ascii'))
    recv11= clientSocket.recv(1024)

    # Send QUIT command and handle server response.
    clientSocket.send(quitMessage.encode('ascii'))
    recv13 = clientSocket.recv(1024)

    clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')