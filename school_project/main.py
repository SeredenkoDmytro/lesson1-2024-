from tkinter import Tk, Button
root = Tk()
root.geometry('600x400')

def click():
    button['text'] = '9-I клас'
    button['width'] = 80
    button['fg'] = 'green'
    button['state'] = 'disabled'

button = Button(root, text='Кнопка 1234', height=3, width=15, command=click)
button.pack(pady=30)

root.mainloop()
