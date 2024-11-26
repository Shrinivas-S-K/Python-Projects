from tkinter import *
def pal():
    x=entry.get()
    if x!="":
        lap=x[::-1]
        if x==lap:
            Label(root,text="\nis a palindrome").pack()
        else:
            Label(root,text="\nis not a palindrome").pack()

root=Tk()
root.title("Palindrome")
root.geometry("400x300")
Label(root,text='Enter the word').pack()
entry=Entry(root)
entry.pack()

Button(root,text="Submit",command=pal,).pack()

root.mainloop()