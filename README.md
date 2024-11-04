# Network-Scanner
The Network Scanner is a simple yet efficient tool designed to identify and list devices within a network. This project offers functionalities for detecting live hosts, scanning open ports, and retrieving basic information about connected devices. It serves as an excellent resource for learning network fundamentals, enhancing security awareness, and exploring network configurations.


# Features
Simple TCP port scanner, designed to test which ports on a target IP address are open and accepting connections. The use of multithreading helps make the scanning process efficient by testing multiple ports at once.
Features.
  TCP Port Scanning: Efficiently tests which ports on a target IP address are open and accepting connections.
Multithreading Support: Utilizes multithreading to accelerate the scanning process by testing multiple ports simultaneously.
User-Friendly Interface: Supports user-defined inputs for IP addresses and port ranges, making it easy to customize scans.
Open Port Reporting: Displays a comprehensive list of open ports when found, enhancing visibility into network accessibility.

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


# DISCLAIMER 
This tool is intended for ethical use only. Please ensure that you have explicit permission to test any networks you are scanning. Unauthorized port scanning may be illegal and is considered unethical..

# LICENSE
This project is licensed under the Apache License.

# ABOUT ME 
My name is Mthobisi Maphumulo, and I am a passionate cybersecurity enthusiast currently pursuing a degree in Computer Science and Applied Mathematics at the University of Witwatersrand. I have hands-on experience in network troubleshooting, technical support, and cybersecurity labs. With a strong foundation in computer science and applied mathematics, I am driven to expand my expertise in cybersecurity and network defense. My interests include exploring network and cloud security, as well as contributing to open-source projects in the field.
