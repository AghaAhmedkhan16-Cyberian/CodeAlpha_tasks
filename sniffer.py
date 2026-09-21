from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        
        print(f"[-] Packet: {src_ip} -> {dst_ip} | Protocol: {proto}")
        
        if packet.haslayer(TCP):
            print(f"    [TCP Port] Src: {packet[TCP].sport} | Dst: {packet[TCP].dport}")
        elif packet.haslayer(UDP):
            print(f"    [UDP Port] Src: {packet[UDP].sport} | Dst: {packet[UDP].dport}")
print("[*] Starting network sniffer... Press Ctrl+C to stop.")
sniff(prn=packet_callback, store=0)