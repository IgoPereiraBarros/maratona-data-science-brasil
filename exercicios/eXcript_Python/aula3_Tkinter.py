import tkinter as tk

janela = tk.Tk()
janela.title('Main Frame')

janela['bg'] = 'red'

#width x height + left + right
janela.geometry('250x250+500+200')

janela.mainloop()