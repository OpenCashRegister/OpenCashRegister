#imports
from tkinter import *
print("Tkinter Imported")

from record import sheeto
print("Sheeto Done")

import record

import subprocess


newtagids=[123456789,123456781]

window = Tk()
print("Window Definition")

Total=Label(window,text="Total: $0.00")
Total.pack()
#Func Definition
def tags():
  textlist=[]
  for id in newtagids:
    rownum=sheeto.ids[str(id)]
    row=sheeto.Itemsheet.getRow(rownum)
    pricee=row[2]
    if pricee:
      price=pricee
    else:
      price="0.00"
    name=row[0]
    profit=row[3]
    fulltext=f"{name}| ${price}"
    textlist.append(fulltext)
    Total.config(text="Total: $"+str(float((Total.cget("text")[8:]))+float(price)))
    record.ins(id,profit,name)
  newtagids.clear()
  
  return textlist

#some other stufffffffff
newtags=[]
window.title("PiRegister")
window.geometry('700x400')


Items = Listbox(window, height = 20, 
                  width = 30, 
                  bg = "purple",
                  fg = "white")
print("ListBox Definition")

Items.pack() 
print(".pack -ed listbox")

def clr():
  Items.delete(0,'end')
  Total.config(text="$0.00")

Btn =Button(window, text ="NEXT", command = clr)

Btn.pack()

def checkit():
  if len(newtags) > 0:
    for i2 in newtags:
      Items.insert(Items.size(),i2)
  newtags.clear()
  tgs=tags()
  if tgs:
    for i in tgs:
      newtags.append(i)
      window.after(125, checkit)


print("Def checkit")
window.after(1000, checkit)

print("win.after")
window.mainloop()