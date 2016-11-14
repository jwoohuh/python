import socket               # Import socket module
import array

MSGLEN = 8192

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
host = "localhost" # Get local machine name
port = 12345                # Reserve a port for your service.

s.bind((host, port))        # Bind to the port
s.listen(5)                # Now wait for client connection.

print "Waiting for connection..."
c, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr

while True:
	buff = c.recv(MSGLEN)
	print buff
	f = open("check.txt", "a")
	"""
	tofloats = array.array('f', buff)
	floats = tofloats.tolist()
	
	line = []
	num = 0

	for _float in floats:
		num = num + 1
		line.append(str(_float))
		if num % 8 == 0:
			f.write(" ".join(line) + "\n")
			line = []
	f.write("\n")
	"""
	f.write(buff + "\n")
	#print floats
	
c.close()                # Close the connection