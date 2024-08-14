import tkinter as tk
from PIL import Image, ImageTk


def count_arttir():
    currently_number=count.get()
    count.set(currently_number+1)
    update_text()

def sifirla():
    currently_number=count.get()
    count.set(currently_number-currently_number)
    update_text()

def count_azalt():
    currently_number=count.get()
    count.set(currently_number-1)
    update_text()

def update_text():
    sayac.config(text=str(count.get()))


root = tk.Tk()
root.geometry("330x200")
root.title("Sayaç")

count = 0
count = tk.IntVar()

canvas = tk.Canvas(root, bg='white',width=2000,height=1500)
canvas.pack(fill=tk.BOTH, expand=True)

offset=100


arttir_button = tk.Button(root, command=count_arttir, padx=15, pady=0,bg='red',text='+',activebackground='red', relief='flat',  borderwidth=0,font=("Helvetica", 13,"bold"))
arttir_button.place(x=75-24, y=37-14)

azalt_button = tk.Button(root,command=count_azalt,padx=15,pady=0,bg='blue',text='-',activebackground='blue', relief='flat', borderwidth=0,font=("Helvetica", 13, "bold"))
azalt_button.place(x= 265-24, y=37-14)

sifirla_button = tk.Button(root, command=sifirla, padx=11,pady=0,bg='green',text='0',activebackground='green', relief='flat', borderwidth=0,font=("Helvetica", 13, "bold"))
sifirla_button.place(x=265-120, y=37+27)


sayac = tk.Label(root, text='0',font=("Arial", 15) )
sayac.place(x=75+84,y=37-14)

oval=canvas.create_oval(30, 18, 120, 56, outline='red', fill='red', width=2)

coords = canvas.coords(oval)
x1, y1, x2, y2 = coords

center_x = (x1 + x2) / 2
center_y = (y1 + y2) / 2


center_x2 = ( x1 + (x2 - x1) + offset+ x2 + (x2 - x1) + offset) / 2
center_y2 = (y1 + y2) / 2

oval2 = canvas.create_oval(x1 + (x2 - x1) + offset, y1, x2 + (x2 - x1) + offset, y2,  outline='blue', fill='blue')
oval3 = canvas.create_oval(117,60,208,94, outline='green', fill='green')



root.mainloop()