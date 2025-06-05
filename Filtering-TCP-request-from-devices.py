from scapy.all import sniff,TCP,IP
try :
 usrinput=int(input("Enter how many packets you want to filter (eg : 10000):"))
except ValueError :
    print("Only integer value accepted !!")
def tcp_filter(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        ip_layer=packet[IP]
        tcp_layer=packet[TCP]
        print(f"{ip_layer.src}:{tcp_layer.sport} --> {ip_layer.dst}:{tcp_layer.dport}")

sniff(filter="tcp",count=usrinput,prn=tcp_filter,iface="Wi-Fi")
      
    