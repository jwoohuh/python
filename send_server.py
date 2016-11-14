import socket               # Import socket module
import array

MSGLEN = 2048

def send(self, msg):
	totalsent = 0
	while totalsent < MSGLEN:
		sent = self.sock.send(msg[totalsent:])
		if sent == 0:
			raise RuntimeError("socket connection broken")
		totalsent = totalsent + sent

def receive(sock):
	chunks = []
	bytes_recvd = 0
	while bytes_recvd < MSGLEN:
		chunk = sock.recv(min(MSGLEN - bytes_recvd, 2048))
		#bytes = sock.recv(4)
		#chunk = sock.recv(4)
		if chunk == b'':
			raise RuntimeError("socket connection broken")
		chunks.append(chunk)
		bytes_recvd = bytes_recvd + len(chunk)
	return b''.join(chunks)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object
host = "" # Get local machine name
port = 12345                # Reserve a port for your service.

s.bind((host, port))        # Bind to the port
s.listen(5)                # Now wait for client connection.

print "Waiting for connection..."
c, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr

while True:
	buff = "Hello World! Python and Android Socket communication"
	sent = c.send(buff)
	print str(sent) + " bytes sent"
	
c.close()                # Close the connection