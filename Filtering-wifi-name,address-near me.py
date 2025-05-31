from scapy.all import sniff,Dot11Beacon,Dot11Elt

def filter(packet):
    if packet.haslayer(Dot11Beacon):
        ssid=packet[Dot11Elt].info.decode(error='ignore')
        bssid=packet[Dot11Beacon].addr3
    print(f"SSID:{ssid},BSSID:{bssid}")



sniff(iface="wlan0mon",prn=filter)