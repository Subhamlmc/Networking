from scapy.all import sniff,DNS,IP
try :
 usrinput=int(input("Enter how many packets you want to filter (eg : 10000):"))
except ValueError :
    print("Only integer value accepted !!")
def dns_filter(packet):
    if packet.haslayer(IP) and packet.getlayer(DNS).qr==0:
        ip_layer=packet[IP]
        dns_layer=packet[DNS]
        print(f"DNS QUERY : {ip_layer.src} is visting {dns_layer.qd.qname.decode()}")

sniff(filter="udp port 53",count=usrinput,prn=dns_filter,iface="Wi-Fi")