import tkinter as tk
import tkinter.scrolledtext as tkst

text_name = "2_3.text"

def save():
    f = open(text_name,'w',encoding='utf-8')
    f.write(t.get(0.0,tk.END))
    f.close()
def load():
    t.delete('1.0','end-1c')
    f=open(text_name,'r',encoding='utf-8')
    for line in f:
        t.insert(tk.END,line)
    f.close()

win = tk.Tk()

btn_save = tk.Button(win,text='save',command=save)
btn_save.place(x=0,y=0)

btn_load = tk.Button(win,text='load',command=load)
btn_load.place(x=60,y=0)


t= tkst.Text(win)
t.place(x=0,y=30)

win.mainloop()