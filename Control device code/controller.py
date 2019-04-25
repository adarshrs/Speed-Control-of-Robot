import motor
import time
import pigpio as io


class controller:
	def __init__(self,numMot):
		self.motorInterface = motor.motor()
		self.motorNumber = numMot
		self.currentSpeed = 0
		self.accelerationStep = 10
		self.decelerationStep = -10
		self.timeDelay = 0.01

	def moveForward(self, speed = 50, duration=-1):
		if self.currentSpeed < 0:
			self.stopMoving()

		if self.currentSpeed >= speed:
			for s in range(self.currentSpeed, speed-10, self.decelerationStep):
				for m in range(0,self.motorNumber):
					self.motorInterface.setSpeed(s,m+1)
					time.sleep(self.timeDelay)

		elif self.currentSpeed < speed:
			for s in range(self.currentSpeed, speed+10, self.accelerationStep):
				for m in range(0,self.motorNumber):
					self.motorInterface .setSpeed(s,m+1)
					time.sleep(self.timeDelay)

		self.currentSpeed = speed

		if duration>0:
			time.sleep(duration)
			self.stopMoving()

	def moveReverse(self,speed = 50,duration=-1):
		if self.currentSpeed > 0:
			self.stopMoving()

		if abs(self.currentSpeed) > speed:
			for s in range(self.currentSpeed, speed-10, self.decelerationStep):
				for m in range(0,self.motorNumber):
					self.motorInterface.setSpeed(s,m+1)
					time.sleep(self.timeDelay)

		elif abs(self.currentSpeed) < speed:
			for s in range(self.currentSpeed, speed+10, self.accelerationStep):
				for m in range(0,self.motorNumber):
					self.motorInterface.setSpeed(s,m+1)
					time.sleep(self.timeDelay)

		self.currentSpeed = speed

		if duration>0:
			time.sleep(duration)
			self.stopMoving()

	def stopMoving(self):
		if self.currentSpeed > 0:
			for s in range(self.currentSpeed, -10, self.decelerationStep):
				for m in range(0,self.motorNumber):
					self.motorInterface.setSpeed(s,m+1)
					time.sleep(self.timeDelay)
			self.currentSpeed = 0

		elif self.currentSpeed < 0:
			for s in range(self.currentSpeed, 10, -1*self.decelerationStep):
				for m in range(0,self.motorNumber):
					self.motorInterface.setSpeed(s,m+1)
					time.sleep(self.timeDelay)
			self.currentSpeed = 0

	def turnLeft(self):
		self.motorInterface.setSpeed(int(self.currentSpeed*0.6), 1)
		self.motorInterface.setSpeed(int(self.currentSpeed*0.6), 3)
		self.motorInterface.setSpeed(int(self.currentSpeed*0.6), 5)
		self.motorInterface.setSpeed(int(self.currentSpeed*1.4), 2)
		self.motorInterface.setSpeed(int(self.currentSpeed*1.4), 4)
		self.motorInterface.setSpeed(int(self.currentSpeed*1.4), 6)

	def quit(self,event):
		self.stopMoving()
		for m in range(0,self.motorNumber):
			m.quit()
		exit()
