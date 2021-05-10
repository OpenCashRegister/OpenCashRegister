import zmq
import time
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:1660")
tagsss=["123456789","1010","102938470"]
while True:
  socket.recv()
  socket.send(('|'.join(tagsss)).encode('utf-8'))
  time.sleep(0.1)