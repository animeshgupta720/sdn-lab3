#!/usr/bin/env python

from scapy.all import *
from scapy.contrib.openflow3 import OpenFlow3

pcapFile='new_switch.pcapng'
i = 0
n=0
pkts = rdpcap(pcapFile)

#For a feature_reply packet the type value == 6, so my script is detecting a feature reply packet.
#print(pkts[153][3].type)

for count in pkts:
	n = n+1

print("\n")
print("The total number of packets in the capture is {}".format(n))
print("\n")
#print(pkts[2][2].sport)
#	print("success")
for i in range(1,n):
	try:
		if pkts[i][3].type==6:
			print("Feature_Reply message received from switch. Connection Successful!!")
			print("\n")
			print(pkts[i][3].show)
				
			print("\n")
			print("The DPID of the switch is ==>>  {}".format(pkts[i][3].datapath_id))
			dpid = pkts[i][3].datapath_id
			ip_address=pkts[i][1].src
			break
	except:
		#print("no match, continue check")
		continue
	
#dpid = pkts[i][3].datapath_id
#ip_address=pkts[i][1].src 
result = { dpid : { 'ip_address' : ip_address, 'status' : 'connected' } }

print(result)

file1 = open("connected.txt","w")
file1.write(str(result))
file1.write("\n")
print("File updated successfully!!")
file1.close()

print("\n")





