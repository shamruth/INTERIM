import tkinter
window=tkinter.Tk()
window.title("GUI")
label=tkinter.Label(window,text="ENTER THE TASKS TO ADD")
label.grid(column=1,row=1)
label2=tkinter.Label(window)
label2.grid(column=1,row=4)
text_box=tkinter.Entry(window,width=10)
text_box.grid(column=1,row=2)
cvar=tkinter.IntVar()
def bclicked():
    result=text_box.get()
    c=tkinter.Checkbutton(window,text=result,variable=cvar)
    c.grid()
button=tkinter.Button(window,text="ENTER",command=bclicked)
button.grid(column=1,row=3)
window.mainloop()
    