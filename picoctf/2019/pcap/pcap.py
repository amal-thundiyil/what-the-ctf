from scapy.all import *

pcap = rdpcap("./capture.pcap")

flag = []
for p in pcap[UDP]:
    try:
        if (p[IP].src == "10.0.0.2" and p[IP].dst == "10.0.0.12"):
            flag.append(p[Raw].load.decode("utf-8"))
    except IndexError:
        pass

print("".join(flag))
