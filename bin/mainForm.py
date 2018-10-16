import tkinter as tk

window = tk.Tk()
window.title("Ping Monitor")
window.geometry("600x800")

shatianVar = tk.IntVar()
foshaVar = tk.IntVar()

def node_selection():
    pass

shatian = tk.Checkbutton(window,text='沙田服务器',height=1,width=11,variable = shatianVar,offvalue=0,font=("Arial", 16),bg="blue",command=node_selection)
shatian.place(x=20,y=20)

foshan = tk.Checkbutton(window,text='佛山服务器',variable = foshaVar,offvalue=0,font=("Arial", 16),height=1,width=11,bg="yellow",command=node_selection)
foshan.place(x=185,y=20)


window.mainloop()