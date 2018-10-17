import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Ping Monitor")
window.geometry("600x800")

shatianVar = tk.IntVar()
foshaVar = tk.IntVar()

def node_selection():
    pass

shatian = tk.Checkbutton(window,text='沙田服务器',height=1,width=11,variable = shatianVar,offvalue=0,font=("Arial", 16),bg="blue")
shatian.place(x=20,y=20)

foshan = tk.Checkbutton(window,text='佛山服务器',variable = foshaVar,offvalue=0,font=("Arial", 16),height=1,width=11,bg="yellow")
foshan.place(x=185,y=20)

test = tk.Button(window,height=1,width=79,text="开 始 测 试",command=node_selection).place(x=20,y=60)

frm_info = tk.Frame(window,height=700,width=565,bg="red")
frm_info.place(x=20,y=100)

# 创建表格
dataInfo = ttk.Treeview(frm_info)

# 定义列
dataInfo['columns'] = ['status','ipAddress','delay','packetLoss']
dataInfo.pack()

# 设置列宽度
dataInfo.column("status",width=100)
dataInfo.column("ipAddress",width=100)
dataInfo.column("delay",width=100)
dataInfo.column("packetLoss",width=100)

# 设置列名
dataInfo.heading('status',text="状态")
dataInfo.heading('ipAddress',text="IP")
dataInfo.heading('delay',text="延迟")
dataInfo.heading('packetLoss',text="丢包率")

dataInfo.insert('',0,values=('运行','162.247.98.132','0.32ms','0%'))

window.mainloop()