from tkinter import Tk, Label, Button
from PIL import Image, ImageTk

global blue
blue = False
global green
green = False
global red
red = False


def comando(op):
	global blue
	global green
	global red

	if (op == 1 and blue == False):
		print('Led azul ligado')
		icon_led_blue = ImageTk.PhotoImage(file='imgs/azul.jpg')
		button1.config(image=icon_led_blue, highlightthickness=0, bd=0)
		button1.image = icon_led_blue
		blue = True

	elif (op == 1 and blue == True):
		print('Led azul desligado')
		icon1 = ImageTk.PhotoImage(file='imgs/preto.jpg')
		button1.config(image=icon1, highlightthickness=0, bd=0)
		button1.image = icon1
		blue = False

	elif (op == 2 and green == False):
		print('Led verde ligado')
		icon_led_gren = ImageTk.PhotoImage(file='imgs/verde.jpg')
		button2.config(image=icon_led_gren, highlightthickness=0, bd=0)
		button2.image = icon_led_gren
		green = True

	elif (op == 2 and green == True):
		print('Led verde desligado')
		icon2 = ImageTk.PhotoImage(file='imgs/preto.jpg')
		button2.config(image=icon2, highlightthickness=0, bd=0)
		button2.image = icon2
		green = False

	elif (op == 3 and red == False):
		print('Led vermelho ligado')
		icon_led_red = ImageTk.PhotoImage(file='imgs/vermelho.jpg')
		button3.config(image=icon_led_red, highlightthickness=0, bd=0)
		button3.image = icon_led_red
		red = True

	elif (op == 3 and red == True):
		print('Led vermelho desligado')
		icon3 = ImageTk.PhotoImage(file='imgs/preto.jpg')
		button3.config(image=icon3, highlightthickness=0, bd=0)
		button3.image = icon3
		red = False


windows = Tk()
windows.title('Arduino')

windows.geometry('750x750')

text1 = Label(text='led azul', fg='blue')
text1.place(x=70, y=70)

icon_led_black1 = ImageTk.PhotoImage(file='imgs/preto.jpg')
button1 = Button(text='Ligar led azul', command=lambda: comando(1))
button1.config(image=icon_led_black1, highlightthickness=0, bd=0)
button1.place(x=50, y=90)

text2 = Label(text='led verde', fg='green')
text2.place(x=230, y=70)

icon_led_black2 = ImageTk.PhotoImage(file='imgs/preto.jpg')
button2 = Button(text='Ligar led verde', command=lambda: comando(2))
button2.config(image=icon_led_black2, highlightthickness=0, bd=0)
button2.place(x=210, y=90)

text3 = Label(text='led vermelho', fg='red')
text3.place(x=400, y=70)

icon_led_black3 = ImageTk.PhotoImage(file='imgs/preto.jpg')
button3 = Button(text='Ligar led vermelho', command=lambda: comando(3))
button3.config(image=icon_led_black3, highlightthickness=0, bd=0)
button3.place(x=385, y=90)

windows.mainloop()