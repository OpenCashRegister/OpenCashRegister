import logging
from tkinter import *
from record import sheeto
import record
import subprocess
import zmq
import subprocess

idd=input("ID: ")
sheeto.id=idd
logging.basicConfig(format='%(levelname)s:%(message)s')
logging.info("Started")

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:1660")

logging.info("ZMQ Socket Initiated")

newtagids=[]
window = Tk()
Total=Label(window,text="Total: $0.00")
Total.pack()
prevlen=0


def updatte():
  socket.send(b'o')
  lst=socket.recv().decode().split("|")
  if len(lst) > prevlen:
    frst=prevlen
    last=len(lst)-1
    for indx in range(frst,last):
      newtagids.append(lst[indx])



def tags():
  textlist=[]
  updatte()
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


newtags=[]
window.title("PiRegister")
window.geometry('700x400')


Items = Listbox(window, height = 20, 
                  width = 30, 
                  bg = "purple",
                  fg = "white")


Items.pack() 


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
  window.after(333, checkit)


window.after(1000, checkit)


window.mainloop()