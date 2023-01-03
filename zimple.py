import socket

def port_scanner(host, port_range):
  for port in port_range:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.settimeout(0.5)
      result = s.connect_ex((host, port))
      if result == 0:
        print("Port {} is open".format(port))
      s.close()
    except:
      pass

# This code will scan the first 1024 ports on the host "www.example.com" and print out which ones are open. 
# You can adjust the range of ports to scan by changing the arguments to the range function.
port_scanner("www.example.com", range(1, 1024))
