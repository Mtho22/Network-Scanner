import socket
from concurrent.futures import ThreadPoolExecutor

# The scan port function attempts to connect to a port and a specific ip address
# if the port is open it will return port number otherwise none

def scan_port(ip, port):
    try:
        #create a socket using IPV4 and TCP
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # timeout of 1 second to find a connection 
            result = sock.connect_ex((ip,port)) # attempts to connect to the IP tuple
            if result == 0: #if connect_ex returns 0 means a port is open
                return port

    except Exception:
        pass
    return None # returns none if the port is closed

#this function now scans a Range of ports given a IP address to find open ports
def scan_ports(ip,start_port,end_port):
    open_ports =[] # list to store open ports found
    #create a thread pool with max of 100 threads to run port scans concurrently
    with ThreadPoolExecutor(max_workers=100) as executor:
        #submit the scan_port tasks for each port
        futures = [executor.submit(scan_port, ip, port) for port in range(start_port, end_port + 1)]
        for future in futures:
            port=future.result()
            if port: #if port is returned, its open, so add it to open ports
                open_ports.append(port)
    return open_ports # returns a list of open ports
            
    # this the mai function to gather user input and  start the port scanning process
def main():
    #prompt the user to enter IP ADDRESS and port range
    target_ip=input("enter the IP ADDRESS to scan: ")
    start_port=int(input("enter the starting port number: "))
    end_port=int(input("enter the ending port number: "))
    print(f"Scanning {target_ip} from port {start_port} to {end_port}...")

    # calls the scan_ports function and stores the results
    open_ports = scan_ports(target_ip,start_port,end_port)

    #print the list of open ports or a message if no ports
    if open_ports:
             print(f"Open ports :{open_ports}") 
    else:
            print("No open ports found ") 

            #runs the main fucntion if this script is done directly
if __name__ =="__main__":
    main()
            
