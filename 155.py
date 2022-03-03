from tkinter import *
import random
root=Tk()
root.geometry("400x400")
root.title("dictionary")
dictionary={"colour":["maroon1","lawn green","cyan","magenta2","purple1","springgreen2","deep pink","chocolate1"]}

def change_background():
    random_num=random.randint(0,7)
    print(dictionary["colour"][random_num])
    root.configure(background=dictionary["colour"][random_num])
    

btn=Button(root,text="colours",command=change_background)
btn.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()

