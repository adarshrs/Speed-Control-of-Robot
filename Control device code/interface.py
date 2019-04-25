import controller
import tkinter as tk
import time
#----------------------------------------------------------------------
#	Initialize motor pin numbers and create motor controller object
#----------------------------------------------------------------------

C = controller.controller(6)

#----------------------------------------------------------------------
#	Create GUI: Enter speed of bot from 0-99
#----------------------------------------------------------------------

root = tk.Tk()

frame1 = tk.Frame(root, width = 200, height = 200)
frame1.grid(row=1,column=1)

title1 = tk.Label(frame1,text = "Bot speed", font = 'Helvetica 12 bold')
title1.grid(row=1, column=1)

nSpeedFrame = tk.Frame(frame1, width = 200)
nSpeedFrame.grid(row=2,column=1)
speed_label = tk.Label(nSpeedFrame,text = "Set speed: ")
speed_label.grid(row=1,column=1)

cspeedframe = tk.Frame(frame1, width = 200)
cspeedframe.grid(row=3,column=1)
currentSpeed = tk.Label(cspeedframe,text = "Current Speed: ")
currentSpeed.grid(row=1,column=1)

val = tk.StringVar()
val.set(str(C.currentSpeed))

currentSpeedVal = tk.Label(cspeedframe,textvariable = val)
currentSpeedVal.grid(row=1,column=2)

#	Validate if entered value is numeric between -99 and +99
def validate(P):
	if str.isdigit(P) or P == "":
		if len(P)<3:
			return True
		else:
			return False
	elif (P[0] == "-" and (str.isdigit(P[1:])) or P[1:]==""):
		if len(P)<4:
			return True
		else:
			return False
	else:
		return False


vcmd = (root.register(validate))

speed = tk.Entry(nSpeedFrame, validate='all', validatecommand=(vcmd, '%P'))
speed.grid(row=2,column=1)

#	When enter is pressed, set speed of bot to entered speed
def keyboard(event):
	sp = speed.get()
	try:
		s = int(sp)
	except:
		print("Invalid speed")
		return

	if s>0:
		C.moveForward(s)
	elif s<0:
		C.moveReverse(s)
	else:
		C.stopMoving()

	speed.delete(0, 'end')
	val.set(str(C.currentSpeed))

def turnleft():
	C.turnLeft()
	time.sleep(3)
	C.stopMoving()

tl = tk.Button(root,text="Turn Left",command=turnleft)
tl.grid(row=2,column=1)

root.bind("<Return>", keyboard)
root.bind("<Escape>", C.quit)

root.mainloop()
