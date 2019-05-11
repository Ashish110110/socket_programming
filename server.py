import socket
import sys
import excel as xl
import pickle


HOST = "127.0.0.1"
PORT = 9999
ask="Enter the subject for which you want to search the lectures"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
print("Listening ...")
while True:
    conn, addr = s.accept()
    print("[+] Client connected: ", addr)
    conn.send("Enter the subject for which you want to search the lectures")
    frp=conn.recv(1024)
    ssz=conn.recv(1024)
    # get file name to download
    f = open("rast.xlsx", "wb")
    for i in range(int(ssz)):
        # get file bytes
        data = conn.recv(1)
        if not data:
            break
        # write bytes on file
        f.write(data)
    f.close()
    rr=xl.func(frp)
    data=pickle.dumps(rr)
    conn.send(data)
    # close connection
    conn.close()
    print("[-] Client disconnected")
    s.close()
    sys.exit(0)
