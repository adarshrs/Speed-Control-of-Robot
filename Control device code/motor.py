import socket

class motor ():
	def __init__(self):
		self.s = socket.socket()
		self.port = 1234
		self.s.connect(('192.168.43.63', self.port))

	def setSpeed(self,speed,motorNumber):
		sp = str(speed)
		if speed==0:
			sp = "+00"
		elif speed>0:
			sp = "+" + sp
		sp = str(motorNumber) + " " + sp
		self.s.send(sp.encode('ASCII'))

	def quit(self):
		self.s.send(b'iquit')
		self.s.close()
