from scapy.all import sniff,Dot11  
lists=set()
def listing(packet):
    if packet.haslayer(Dot11) and packet.type==2 :
        client=packet.addr2
        if client and client not in lists :
            lists.add(client)
            for mac in lists :
                print(mac)
    
    
sniff(iface="wlan0mon",prn=listing)