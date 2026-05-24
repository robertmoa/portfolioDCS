from scapy.all import sniff, IP, ICMP

malicious_ips = ["100.74.0.1"]
print("===ICMP ANALYSER===")
print("This program is designed to analyse incoming ICMP packets with\nour super secret threat intelligence analysis system (a list)")

def analysis_on(packet):
    if packet.haslayer(ICMP):
        src = packet[IP].src

        print(f"Ping from {src}, Analysing IP for potential threats...")

        if src in malicious_ips:
            print(f"[ALERT] : {src} has been detected as a malicious IP.")

sniff(prn=analysis_on)

