# Network-Scanner
A simple and efficient network scanner built to identify and list devices within a network. This project provides functionalities for detecting live hosts, scanning open ports, and retrieving basic information about connected devices. Ideal for learning network basics, enhancing security awareness, and exploring network configurations.


# Features
Simple TCP port scanner, designed to test which ports on a target IP address are open and accepting connections. The use of multithreading helps make the scanning process efficient by testing multiple ports at once.
Features.
    Scans a range of ports on a specified IP address
    Uses multithreading to increase the scanning speed
    Displays a list of open ports if found
    Supports user-defined IP and port range inputs

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
 1. Clone the Repository: Start by cloning the repository to your local machine using Git. Open your terminal or command prompt and run:
    git clone https://github.com/Mtho22/Network-Scanner.git

2. Verify Python version :Ensure you have Python 3.x installed. You can check your Python version by running: 
   python --version

3. Run the Tool:

   python3 Networkscanner.py 
   or python Networkscanner.py

4. Enter the Target IP address 
   Enter the IP address to scan: 192.168.1.1 Enter the starting port number: 1 Enter the ending port number: 1024 Scanning 192.168.1.1 from port 1 to 1024... Open ports: [22, 80, 443]


# DISCLAIMER 
Use this tool responsibly and only on networks that you own or have explicit permission to test. Unauthorized port scanning on networks may be illegal and is considered unethical.

# LICENSE
This project is licensed under the Apache License

# ABOUT ME 
Im Mthobisi Maphumulo, a passionate cybersecurity enthusiast currently studying Computer Science and Applied Mathematics at the University of Witwatersrand. I have hands-on experience in network troubleshooting, technical support, and cybersecurity labs. With a solid foundation in computer science and applied mathematics, I am driven to expand my expertise in cybersecurity and network defense. My interests include exploring network and cloud security, as well as contributing to open-source projects in the field.
