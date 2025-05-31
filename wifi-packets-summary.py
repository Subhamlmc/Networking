from scapy.all import sniff ,Dot11
 
def summary(packet):
    if packet.haslayer(Dot11):
        print(packet.summary())
        


sniff(iface="wlan0mon",prn=summary,count=100)