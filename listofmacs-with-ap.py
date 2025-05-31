from scapy.all import sniff,Dot11 
lists=set()
def macwithap(packet):
    if packet.haslayer(Dot11) and packet.type==2 :
        client=packet.addr1
        ap=packet.addr2
        if client and ap and (client,ap) not in lists:
            lists.add((client,ap))
            for macwithaps in lists.items() :
                print(macwithaps)
            
sniff(iface="wlan0mon",prn=macwithap)