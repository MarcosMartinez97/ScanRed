# ScanRed
- Script made in python3
- The objetive of this is to simulate a console command to scan the devices connected to the ip provided for the user and bring back a list of the ips of the devices which 
  are active
- The way to use the script is as follow "python3 pingprov.py -t ip/mask"
- Example of using > pingprov.py -t 192.168.0.0/24 (In this case the program will execute ping to 192.168.0.x)
- The scan depends on the type of mask, the options are 8,16,24. Dynamics mask are not allowed
- For more information you have the help option putting -h "python3 pingprov.py -h"
- It has an optional parameter but by the moment it does nothing
