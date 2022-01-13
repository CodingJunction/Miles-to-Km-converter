from tkinter import *

def conv():
    inp=float(ip.get())
    km=inp*1.609
    l4.config(text=str(km))




screen=Tk()
screen.title("Miles to Km Converter")
screen.minsize(300,200)
screen.config(padx=20,pady=20)
ip=Entry(width=7)
print(ip.get())
ip.grid(row=0,column=1)

l2=Label(text="Miles")
l2.grid(row=0,column=2)

l1=Label(text="Is equal to")
l1.grid(row=1,column=0)


b=Button(text="Calculate",command=conv)
b.grid(row=2,column=1)

l3=Label(text="Km")
l3.grid(row=1,column=2)
res=0
l4=Label(text=str(res))
l4.grid(row=1,column=1)
# ip=Entry()
# print(ip.get())
# # ip.size(width=10)
# ip.pack(side="top")

# l1=Label(text="Km")
# l1.pack(side="left")











screen.mainloop()