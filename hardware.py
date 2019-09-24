#!usr/bin/env python
import subprocess
import os
sudopass ="sdn123"
os.system("echo %s | sudo -S %s" %(sudopass,"sudo ovs-ovctl add-br br1"))
os.system("echo %s | sudo -S %s" %(sudopass,"sudo ovs-ovctl add-port br1 eno3"))
os.system("echo %s | sudo -S %s" %(sudopass,"sudo ovs-ovctl add-port br1 eno4"))
os.system("echo %s | sudo -S %s" %(sudopass,"sudo ifconfig  br1 20.0.0.3 netmask 255.255.255.0"))
os.system("echo %s | sudo -S %s" %(sudopass,"sudo ip link set br1 up"))
os.system("echo %s | sudo -S %s" %(sudopass,"sudo service networking restart"))
os.system("echo %s | sudo -S %s" %(sudopass,"sudo ovs-ovctl add-br br2"))
os.system("echo %s | sudo -S %s" %(sudopass,"sudo ovs-ovctl add-port br2 eno2"))
os.system("echo %s | sudo -S %s" %(sudopass,"sudo ifconfig  br2 10.20.30.2 netmask 255.255.255.0"))
os.system("echo %s | sudo -S %s" %(sudopass,"sudo ip link set br2 up"))
os.system("echo %s | sudo -S %s" %(sudopass,"sudo service networking restart"))
os.system("echo %s | sudo -S %s" %(sudopass,"sudo ovs-vsctl set-controller br2 tcp:10.20.30.2:6633"))
os.system("echo %s | sudo -S %s" %(sudopass,"sudo ovs-vsctl set bridge br1 protocols=OpenFlow10"))
p1 = os.system("echo %s | sudo -S %s" %(sudopass,"sudo ovs-vsctl show"))
p2 = os.system("echo %s | sudo -S %s" %(sudopass,"sudo ovs-ofctl dump-flows br1"))
print(p1)
print(p2)

