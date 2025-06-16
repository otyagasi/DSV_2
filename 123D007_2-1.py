import tkinter as tk
import tkinter.scrolledtext as tkst

def char_count():
    count = t.get(0.0,tk.END)
    intcount = len(count)-1
    ravel["text"] = str(intcount)+"文字"

win = tk.Tk()

ravel = tk.Label(text='0文字',bg="white")
ravel.place(x=50,y=5)

btn = tk.Button(win,text='count',command=char_count)
btn.place(x=0,y=0)

t= tkst.Text(win)
t.place(x=0,y=30)

win.mainloop()