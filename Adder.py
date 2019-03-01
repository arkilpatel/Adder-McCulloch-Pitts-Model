from tkinter import *

flagA = 0
flagB = 0

ans = []

listA = []
listB = []
carry = 0

n11 = 0
n12 = 0
n21 = 0
n22 = 0
n23 = 0
n31 = 0
n41 = 0
n42 = 0
n43 = 0
n51 = 0
n52 = 0

w111 = 2
w112 = -1
w113 = 1
w121 = -1
w122 = 2
w123 = 1
w131 = -1
w132 = 2
w133 = 1

w211 = 2
w221 = 2
w232 = 2

w311 = 2
w312 = -1
w313 = 1

w411 = 2
w421 = 2
w432 = 2

def dec_to_bin(x):
	bin_lst = []
	binary = str(bin(x)[2:])
	for i in binary:
		bin_lst.append(int(i))
	return bin_lst

# gui Window
window = Tk()

# title of GUI Window 
window.title("McCulloch-Pitts Model of Neural Network for Adder")

# dimensions of GUI window
window.geometry("1200x1000")

C = Canvas(window, bg = "blue", height = 1000, width = 1200)

neuron11 = C.create_oval(50, 50, 100, 100, fill = 'red')
neuron12 = C.create_oval(50, 200, 100, 250, fill = 'red')
neuron13 = C.create_oval(50, 350, 100, 400, fill = 'red')

line111 = C.create_line(100, 75, 300, 75, fill = 'black', width = 3, arrow = LAST)
line112 = C.create_line(100, 75, 300, 225, fill = 'black', width = 3, arrow = LAST)
line113 = C.create_line(100, 75, 300, 375, fill = 'black', width = 3, arrow = LAST)
line121 = C.create_line(100, 225, 300, 75, fill = 'black', width = 3, arrow = LAST)
line122 = C.create_line(100, 225, 300, 225, fill = 'black', width = 3, arrow = LAST)
line123 = C.create_line(100, 225, 300, 375, fill = 'black', width = 3, arrow = LAST)
line131 = C.create_line(100, 375, 800, 75, fill = 'black', width = 3, arrow = LAST)
line132 = C.create_line(100, 375, 800, 225, fill = 'black', width = 3, arrow = LAST)
line133 = C.create_line(100, 375, 325, 550, 800, 375, fill = 'black', width = 3, arrow = LAST, smooth = True)

label111 = Label(window, text=str(w111), font = ("",15))
label111.place(x=180, y=45)

label112 = Label(window, text=str(w112), font = ("",15))
label112.place(x=260, y=160)

label113 = Label(window, text=str(w113), font = ("",15))
label113.place(x=245, y=250)

label121 = Label(window, text=str(w121), font = ("",15))
label121.place(x=260, y=115)

label122 = Label(window, text=str(w122), font = ("",15))
label122.place(x=220, y=195)

label123 = Label(window, text=str(w123), font = ("",15))
label123.place(x=150, y=280)

label131 = Label(window, text=str(w131), font = ("",15))
label131.place(x=720, y=70)

label132 = Label(window, text=str(w132), font = ("",15))
label132.place(x=720, y=250)

label133 = Label(window, text=str(w133), font = ("",15))
label133.place(x=690, y=380)

neuron21 = C.create_oval(300, 50, 350, 100, fill = 'red')
neuron22 = C.create_oval(300, 200, 350, 250, fill = 'red')
neuron23 = C.create_oval(300, 350, 350, 400, fill = 'red')

line211 = C.create_line(350, 75, 550, 225, fill = 'black', width = 3, arrow = LAST)
line221 = C.create_line(350, 225, 550, 225, fill = 'black', width = 3, arrow = LAST)
#line233 = C.create_line(350, 375, 800, 375, fill = 'black', width = 3, arrow = LAST)
line232 = C.create_line(350, 375, 575, 600, 1050, 300, fill = 'black', width = 3, arrow = LAST, smooth = True)

label211 = Label(window, text=str(w111), font = ("",15))
label211.place(x=450, y=120)

label221 = Label(window, text=str(w221), font = ("",15))
label221.place(x=400, y=195)

label232 = Label(window, text=str(w232), font = ("",15))
label232.place(x=1000, y=330)

neuron31 = C.create_oval(550, 200, 600, 250, fill = 'red')

line311 = C.create_line(600, 225, 800, 75, fill = 'black', width = 3, arrow = LAST)
line312 = C.create_line(600, 225, 800, 225, fill = 'black', width = 3, arrow = LAST)
line313 = C.create_line(600, 225, 800, 375, fill = 'black', width = 3, arrow = LAST)

label311 = Label(window, text=str(w311), font = ("",15))
label311.place(x=750, y=120)

label312 = Label(window, text=str(w312), font = ("",15))
label312.place(x=720, y=195)

label313 = Label(window, text=str(w313), font = ("",15))
label313.place(x=760, y=315)

neuron41 = C.create_oval(800, 50, 850, 100, fill = 'red')
neuron42 = C.create_oval(800, 200, 850, 250, fill = 'red')
neuron43 = C.create_oval(800, 350, 850, 400, fill = 'red')

line411 = C.create_line(850, 75, 1050, 150, fill = 'black', width = 3, arrow = LAST)
line421 = C.create_line(850, 225, 1050, 150, fill = 'black', width = 3, arrow = LAST)
line432 = C.create_line(850, 375, 1050, 300, fill = 'black', width = 3, arrow = LAST)

label411 = Label(window, text=str(w411), font = ("",15))
label411.place(x=950, y=80)

label421 = Label(window, text=str(w421), font = ("",15))
label421.place(x=950, y=195)

label432 = Label(window, text=str(w432), font = ("",15))
label432.place(x=950, y=305)

neuron51 = C.create_oval(1050, 125, 1100, 175, fill = 'red')
neuron52 = C.create_oval(1050, 275, 1100, 325, fill = 'red')

line523 = C.create_line(1075, 325, 575, 650, 75, 400, fill = 'black', width = 3, arrow = LAST, smooth = True)

label523 = Label(window, text="carry", font = ("",15))
label523.place(x=500, y=515)

labelA = Label(window, text = "Enter First Number: ", font = ("",15))
entA = Entry(window, font = ("",15), width = 15)
labelA.place(x=500, y=670)
entA.place(x=520, y=695)

labelB = Label(window, text = "Enter Second Number: ", font = ("",15))
entB = Entry(window, font = ("",15), width = 15)
labelB.place(x=495, y=750)
entB.place(x=520, y=775)

def L1():
	global n21
	global n22
	global n23

	neuron11 = C.create_oval(50, 50, 100, 100, fill = 'green')
	neuron12 = C.create_oval(50, 200, 100, 250, fill = 'green')
	neuron13 = C.create_oval(50, 350, 100, 400, fill = 'green')

	line111 = C.create_line(100, 75, 300, 75, fill = 'white', width = 3, arrow = LAST)
	line112 = C.create_line(100, 75, 300, 225, fill = 'white', width = 3, arrow = LAST)
	line113 = C.create_line(100, 75, 300, 375, fill = 'white', width = 3, arrow = LAST)
	line121 = C.create_line(100, 225, 300, 75, fill = 'white', width = 3, arrow = LAST)
	line122 = C.create_line(100, 225, 300, 225, fill = 'white', width = 3, arrow = LAST)
	line123 = C.create_line(100, 225, 300, 375, fill = 'white', width = 3, arrow = LAST)
	line131 = C.create_line(100, 375, 800, 75, fill = 'white', width = 3, arrow = LAST)
	line132 = C.create_line(100, 375, 800, 225, fill = 'white', width = 3, arrow = LAST)
	line133 = C.create_line(100, 375, 325, 550, 800, 375, fill = 'white', width = 3, arrow = LAST, smooth = True)

	neuron51 = C.create_oval(1050, 125, 1100, 175, fill = 'red')
	neuron52 = C.create_oval(1050, 275, 1100, 325, fill = 'red')

	line523 = C.create_line(1075, 325, 575, 650, 75, 400, fill = 'black', width = 3, arrow = LAST, smooth = True)

	n21 = w111*n11 + w121*n12
	n22 = w112*n11 + w122*n12
	n23 = w113*n11 + w123*n12

	if n21<2:
		n21 = 0
	else:
		n21 = 1

	if n22<2:
		n22 = 0
	else:
		n22 = 1

	if n23<2:
		n23 = 0
	else:
		n23 = 1

	labeln21 = Label(window, text=str(n21), font = ("",15))
	labeln21.place(x=317, y=62)
	labeln22 = Label(window, text=str(n22), font = ("",15))
	labeln22.place(x=317, y=212)
	labeln23 = Label(window, text=str(n23), font = ("",15))
	labeln23.place(x=317, y=362)	

def L2():
	global n31

	neuron21 = C.create_oval(300, 50, 350, 100, fill = 'green')
	neuron22 = C.create_oval(300, 200, 350, 250, fill = 'green')
	neuron23 = C.create_oval(300, 350, 350, 400, fill = 'green')

	line211 = C.create_line(350, 75, 550, 225, fill = 'white', width = 3, arrow = LAST)
	line221 = C.create_line(350, 225, 550, 225, fill = 'white', width = 3, arrow = LAST)
	#line233 = C.create_line(350, 375, 800, 375, fill = 'white', width = 3, arrow = LAST)
	line232 = C.create_line(350, 375, 575, 600, 1050, 300, fill = 'white', width = 3, arrow = LAST, smooth = True)

	n31 = w211*n21 + w221*n22

	if n31<2:
		n31 = 0
	else:
		n31 = 1

	labeln31 = Label(window, text=str(n31), font = ("",15))
	labeln31.place(x=567, y=212)

def L3():
	global n41
	global n42
	global n43

	neuron31 = C.create_oval(550, 200, 600, 250, fill = 'green')

	line311 = C.create_line(600, 225, 800, 75, fill = 'white', width = 3, arrow = LAST)
	line312 = C.create_line(600, 225, 800, 225, fill = 'white', width = 3, arrow = LAST)
	line313 = C.create_line(600, 225, 800, 375, fill = 'white', width = 3, arrow = LAST)

	n41 = w311*n31 + w131*carry
	n42 = w312*n31 + w132*carry
	n43 = w313*n31 + w133*carry

	if n41<2:
		n41 = 0
	else:
		n41 = 1

	if n42<2:
		n42 = 0
	else:
		n42 = 1

	if n43<2:
		n43 = 0
	else:
		n43 = 1

	labeln41 = Label(window, text=str(n41), font = ("",15))
	labeln41.place(x=817, y=62)
	labeln42 = Label(window, text=str(n42), font = ("",15))
	labeln42.place(x=817, y=212)
	labeln43 = Label(window, text=str(n43), font = ("",15))
	labeln43.place(x=817, y=362)

def L4():
	global n51
	global n52

	neuron41 = C.create_oval(800, 50, 850, 100, fill = 'green')
	neuron42 = C.create_oval(800, 200, 850, 250, fill = 'green')
	neuron43 = C.create_oval(800, 350, 850, 400, fill = 'green')

	line411 = C.create_line(850, 75, 1050, 150, fill = 'white', width = 3, arrow = LAST)
	line421 = C.create_line(850, 225, 1050, 150, fill = 'white', width = 3, arrow = LAST)
	line432 = C.create_line(850, 375, 1050, 300, fill = 'white', width = 3, arrow = LAST)

	n51 = w411*n41 + w421*n42
	n52 = w432*n43 + w232*n23

	if n51<2:
		n51 = 0
	else:
		n51 = 1

	if n52<2:
		n52 = 0
	else:
		n52 = 1

	labeln51 = Label(window, text=str(n51), font = ("",15))
	labeln51.place(x=1067, y=137)
	labeln52 = Label(window, text=str(n52), font = ("",15))
	labeln52.place(x=1067, y=287)


def L5():
	global n11
	global n12
	global carry
	global flagA
	global flagB

	neuron51 = C.create_oval(1050, 125, 1100, 175, fill = 'green')
	neuron52 = C.create_oval(1050, 275, 1100, 325, fill = 'green')

	line523 = C.create_line(1075, 325, 575, 650, 75, 400, fill = 'white', width = 3, arrow = LAST, smooth = True)

	neuron11 = C.create_oval(50, 50, 100, 100, fill = 'red')
	neuron12 = C.create_oval(50, 200, 100, 250, fill = 'red')
	neuron13 = C.create_oval(50, 350, 100, 400, fill = 'red')

	line111 = C.create_line(100, 75, 300, 75, fill = 'black', width = 3, arrow = LAST)
	line112 = C.create_line(100, 75, 300, 225, fill = 'black', width = 3, arrow = LAST)
	line113 = C.create_line(100, 75, 300, 375, fill = 'black', width = 3, arrow = LAST)
	line121 = C.create_line(100, 225, 300, 75, fill = 'black', width = 3, arrow = LAST)
	line122 = C.create_line(100, 225, 300, 225, fill = 'black', width = 3, arrow = LAST)
	line123 = C.create_line(100, 225, 300, 375, fill = 'black', width = 3, arrow = LAST)
	line131 = C.create_line(100, 375, 800, 75, fill = 'black', width = 3, arrow = LAST)
	line132 = C.create_line(100, 375, 800, 225, fill = 'black', width = 3, arrow = LAST)
	line133 = C.create_line(100, 375, 325, 550, 800, 375, fill = 'black', width = 3, arrow = LAST, smooth = True)

	neuron21 = C.create_oval(300, 50, 350, 100, fill = 'red')
	neuron22 = C.create_oval(300, 200, 350, 250, fill = 'red')
	neuron23 = C.create_oval(300, 350, 350, 400, fill = 'red')

	line211 = C.create_line(350, 75, 550, 225, fill = 'black', width = 3, arrow = LAST)
	line221 = C.create_line(350, 225, 550, 225, fill = 'black', width = 3, arrow = LAST)
	#line233 = C.create_line(350, 375, 800, 375, fill = 'black', width = 3, arrow = LAST)
	line232 = C.create_line(350, 375, 575, 600, 1050, 300, fill = 'black', width = 3, arrow = LAST, smooth = True)

	neuron31 = C.create_oval(550, 200, 600, 250, fill = 'red')

	line311 = C.create_line(600, 225, 800, 75, fill = 'black', width = 3, arrow = LAST)
	line312 = C.create_line(600, 225, 800, 225, fill = 'black', width = 3, arrow = LAST)
	line313 = C.create_line(600, 225, 800, 375, fill = 'black', width = 3, arrow = LAST)

	neuron41 = C.create_oval(800, 50, 850, 100, fill = 'red')
	neuron42 = C.create_oval(800, 200, 850, 250, fill = 'red')
	neuron43 = C.create_oval(800, 350, 850, 400, fill = 'red')

	line411 = C.create_line(850, 75, 1050, 150, fill = 'black', width = 3, arrow = LAST)
	line421 = C.create_line(850, 225, 1050, 150, fill = 'black', width = 3, arrow = LAST)
	line432 = C.create_line(850, 375, 1050, 300, fill = 'black', width = 3, arrow = LAST)

	ans.append(n51)
	carry = n52

	#print(listA)
	#print(listB)
	#print(ans)

	if not listA:
		flagA = 1
		n11 = 0
	else:
		n11 = (listA[-1])
		listA.pop()
	if not listB:
		flagB = 1
		n12 = 0
	else:
		n12 = (listB[-1])
		listB.pop()

	labeln11 = Label(window, text=str(n11), font = ("",15))
	labeln11.place(x=67, y=62)
	labeln12 = Label(window, text=str(n12), font = ("",15))
	labeln12.place(x=67, y=212)
	labeln13 = Label(window, text=str(carry), font = ("",15))
	labeln13.place(x=67, y=362)

	if flagA == 1 and flagB == 1:
		ans.append(carry)
		ans.reverse()
		answer = ""
		for i in ans:
			answer = answer+str(i)
		labelAns = Label(window, text = "ANSWER:", font = ("",15))
		labelAns.place(x=560, y=890)
		answerout = Text(window, height = 1, width = 30, font=('Arial', 30, 'bold'))
		answerout.place(x=295, y=910)
		answerout.insert(END,answer)

def Start1():
	global n11
	global n12
	global flagA
	global flagB

	numA = 0
	numB = 0
	if entA.get()!="":
		numA = int(entA.get())
	if entB.get()!="":
		numB = int(entB.get())
	listA[:] = dec_to_bin(numA)
	listB[:] = dec_to_bin(numB)

	if not listA:
		flagA = 1
		n11 = 0
	else:
		n11 = (listA[-1])
		listA.pop()
	if not listB:
		flagB = 1		
		n12 = 0
	else:
		n12 = (listB[-1])
		listB.pop() 

	labeln11 = Label(window, text=str(n11), font = ("",15))
	labeln11.place(x=67, y=62)
	labeln12 = Label(window, text=str(n12), font = ("",15))
	labeln12.place(x=67, y=212)
	labeln13 = Label(window, text=str(carry), font = ("",15))
	labeln13.place(x=67, y=362)

	labelAns = Label(window, text = "ANSWER:", font = ("",15))
	labelAns.place(x=560, y=890)
	answerout = Text(window, height = 1, width = 30, font=('Arial', 30, 'bold'))
	answerout.place(x=295, y=910)
	#labelAns.delete(1.0,END)

btn1 = Button(window, text = "Next", command = L1)
btn1.place(x=50, y=600)

btn2 = Button(window, text = "Next", command = L2)
btn2.place(x=300, y=600)

btn3 = Button(window, text = "Next", command = L3)
btn3.place(x=550, y=600)

btn4 = Button(window, text = "Next", command = L4)
btn4.place(x=800, y=600)

btn5 = Button(window, text = "Next", command = L5)
btn5.place(x=1050, y=600)

btn6 = Button(window, text = "Enter", command = Start1)
btn6.place(x=570, y=830)

C.pack()

window.mainloop()
