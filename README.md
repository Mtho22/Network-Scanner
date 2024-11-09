# Network Port and Protocol-Scanner
The Network and Port Protocol Scanner is a straightforward yet powerful tool designed to identify and list devices within a network. This project offers functionalities for detecting live hosts, scanning open ports, retrieving protocol information, and gathering basic information about connected devices. It is a valuable resource for learning network fundamentals, enhancing security awareness, and exploring network configurations.


# Features
TCP Port Scanning: Efficiently tests which ports on a target IP address are open and accepting connections.
Protocol Identification: Detects the protocol running on each open port, providing more insight into network services.
Multithreading Support: Utilizes multithreading to accelerate the scanning process by testing multiple ports simultaneously.
User-Friendly Interface: Accepts user-defined inputs for IP addresses and port ranges, allowing for easy customization of scans.
Open Port and Protocol Reporting: Displays a detailed list of open ports along with their respective protocols, enhancing network accessibility insights.

# Requirments
To run the Simple Network Port Scanner, you need the following:

    Python: Version 3.x is required. You can download it from python.org.

    Dependencies: This project uses Python's built-in socket library, which is included in the standard library, so no additional installation is necessary.

    Operating System: The tool is compatible with various operating systems, including:
        Windows
        macOS
        Linux

# Installation 
 steps to install and set up the  Network Port Scanner:
Clone the Repository:
Begin by cloning the repository to your local machine. Open your terminal or command prompt and run:

bash

git clone https://github.com/Mtho22/Network-Scanner.git

Verify Python Version:
Ensure that you have Python 3.x installed. You can check your Python version by running:

bash

python --version

Run the Tool:
To execute the scanner, run the following command:

bash

python3 NetworkScanner.py

or

bash

python NetworkScanner.py

4. Input Target Details:
Enter the target IP address and port range as prompted:

yaml

Enter the IP address to scan: 192.168.1.1
Enter the starting port number: 1
Enter the ending port number: 1024
Scanning 192.168.1.1 from port 1 to 1024...
Open ports: [22, 80, 443]

Example output:

yaml
Copy code
Scanning 192.168.1.1 from port 1 to 1024...
Open ports and protocols:
- Port 22: SSH
- Port 80: HTTP
- Port 443: HTTPS


# DISCLAIMER 
This tool is intended for ethical use only. Please ensure that you have explicit permission to test any networks you are scanning. Unauthorized port scanning may be illegal and is considered unethical..

# LICENSE
This project is licensed under the Apache License.

# ABOUT ME 
My name is Mthobisi Maphumulo, and I am a passionate cybersecurity enthusiast currently pursuing a degree in Computer Science and Applied Mathematics at the University of Witwatersrand. I have hands-on experience in network troubleshooting, technical support, and cybersecurity labs. With a strong foundation in computer science and applied mathematics, I am driven to expand my expertise in cybersecurity and network defense. My interests include exploring network and cloud security, as well as contributing to open-source projects in the field.
