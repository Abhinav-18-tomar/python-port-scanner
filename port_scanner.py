import socket
import threading
import tkinter as tk

root=tk.Tk()
root.geometry("500x500")
tk.Label(root,text="**PORT SCANNER**").grid(row=0,column=0)
tk.Label(root,text="Enter Target").grid(row=4,column=0)
target_entry=tk.Entry(root)
target_entry.grid(row=4,column=1)

tk.Label(root,text="Enter Start Port").grid(row=7,column=0)
start_entry=tk.Entry(root)
start_entry.grid(row=7,column=1)

tk.Label(root,text="Enter End Port").grid(row=10,column=0)
end_entry=tk.Entry(root)
end_entry.grid(row=10,column=1)


output= tk.Text(root,height=30,width=62)
output.grid(row=25,column=0,columnspan=3)
def start_scan():
    try:
        target=socket.gethostbyname(target_entry.get())
    except socket.gaierror:
        print("Name resolution error")
        output.insert(tk.END,"\nEnter valid target")
        return
    try:
        start_port= int(start_entry.get())
        end_port=int(end_entry.get())
    except ValueError:
        output.insert(tk.END,"\nEnter valid value")
        return

    if start_port < 1 or end_port > 65535 or start_port > end_port:
        output.insert(tk.END,"Invalid Ports")
        return
    output.insert(tk.END,"\nScanning ports for {}".format(target))
    
    def port_scan(port):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(2)
        conn=s.connect_ex((target,port))
        
        if conn==0:
            output.insert(tk.END,"\nPORT {} IS OPEN ".format (port))

        s.close()

    for port in range(start_port,end_port+1):
        thread = threading.Thread(target=port_scan,args=(port,))
        thread.start()
            
tk.Button(
    root,
    text="START SCAN",
    command=start_scan
).grid(row=13,column=1)

root.mainloop()

