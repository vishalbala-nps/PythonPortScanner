import socket
from prettytable import PrettyTable

item_no = 0
t = PrettyTable(['id','Port'])

print("---------------------")
print("Python Port Scanner")
print("---------------------")

ip = input("Please enter the IP which you would like to scan:")
print()
print("Scanning ports... (this will take a while)")
for i in range(0,65536):
   msocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   msocket.settimeout(1)
   rcode = msocket.connect_ex((ip,i))
   if rcode == 0:
      item_no = item_no+1
      t.add_row([item_no,i])
   msocket.close()
print()
print("List of Open Ports on "+ip+":")
print(t)
print("Number of open ports:"+str(item_no))