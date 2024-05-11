from scapy.all import sniff, wrpcap

def sniff_packets(packet_count=10, filename="captured.pcap"):
    # Capture packets
    packets = sniff(count=packet_count, filter="ip", prn=lambda x: x.summary())
    # Save the captured packets to a file
    wrpcap(filename, packets)
    return packets, filename
