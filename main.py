from tkinter import *
import subprocess
import sheeto
def tags():
  return []
newtags=[]
window = Tk()
window.title("PiRegister")
window.geometry('700x400')
Items = Listbox(window, height = 20, 
                  width = 30, 
                  bg = "purple",
                  fg = "white")
Items.pack()
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
window.after(1000, checkit)
window.mainloop()