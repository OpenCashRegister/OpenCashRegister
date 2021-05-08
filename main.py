from tkinter import *
print("Tkinter Imported")
import subprocess
import sheeto
print("Sheeto Done")
def tags():
	
  return []
newtags=[]
window = Tk()
print("Window Definition")
window.title("PiRegister")
window.geometry('700x400')
Items = Listbox(window, height = 20, 
                  width = 30, 
                  bg = "purple",
                  fg = "white")
Total=Label(window,text="Total: $0.00")
Total.pack()
print("ListBox Definition")
Items.pack()
print(".pack -ed listbox")
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