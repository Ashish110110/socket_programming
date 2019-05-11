import socket
import sys
import os
import pickle


HOST = "127.0.0.1"
PORT = 9999
rr = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("[+] Connected with Server")

# get file name to send
f_send = "SOT_CP_4_TimeTable.xlsx"
# open file
data=s.recv(200)
print(data)
ss = raw_input();
s.send(ss)
statinfo=os.stat("SOT_CP_4_TimeTable.xlsx")
with open(f_send, "rb") as f:
    # send file
    print("[+] Sending file...")
    s.send(str(statinfo.st_size))
    data = f.read()
    s.sendall(data)
    #close connection
    print(rr)
data=s.recv(2048)
rr=pickle.loads(data)
for i in range(rr[-1]):
	print(rr[i])
print ("No of Lectures: " + str(rr[-1])) 
s.close()
print("[-] Disconnected")
sys.exit(0)
