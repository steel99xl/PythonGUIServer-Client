from Tkinter import *
import socket
app = Tk()
app.geometry("200x200")
app.title("Tire PSI Server")
app.grid

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(9999)  # Connection time out limit


def front_left():
        print("First Button")
	c.send("First Buttom")
def front_right():
        print("Second Buttom")
	c.send("Front Right Tire Low")
def back_left():
        print("Third Buttom")
	c.send("Third Button")
def back_right():
        print("Fourth Buttom")
	c.send("Fourth Button")
def close():
	c.close()
	print("connection closed")
btnfl = Button(app)
btnfl.grid()
btnfl.configure(text = "First Button",command = front_left)

btnfr = Button(app)
btnfr.grid()
btnfr.configure(text = "Second Buttom",command = front_right)

btnbl = Button(app)
btnbl.grid()
btnbl.configure(text = "Third Buttom",command = back_left)

btnbr = Button(app)
btnbr.grid()
btnbr.configure(text = "Fourth Buttom",command = back_right)

btnc = Button(app)
btnc.grid()
btnc.configure(text = "Close Connection",command = close)

c, addr = s.accept()     # Establish connection with client.
print('Connection from', addr)

app.mainloop()
