from scapy.all import *
import time

if __name__ == '__main__':
    src_ip = '10.10.1.2'     # Source IP address
    dst_ip = '10.10.1.1'     # Destination IP address
    src_port = 12345         # Source port
    dst_port = 80            # Destination port
    dst_mac = 'a0:36:9f:2a:5c:38'  # MAC address of the target machine
    interface = 'enp3s0f0'   # Interface name on the source machine
    _payload_ = '1'
    num_packets = 2001
    
    packet = Ether(dst=dst_mac) / IP(src=src_ip, dst=dst_ip) / TCP(sport=src_port, dport=dst_port) / Raw(load=_payload_)
    packet_size = len(packet)

    start_time = time.time()
    # sendp(packet, count=num_packets, iface=interface, verbose=False)
    scapy.sendrecv.sendpfast(packet, pps=1000, iface=interface, loop = num_packets, parse_results=1)
    end_time = time.time()
    
    # sendpfast()

    elapsed_time = end_time - start_time
    total_size = num_packets * packet_size
    throughput = (total_size * 8) / (elapsed_time * 1000000)  # Throughput in Mbps

    # print(f"Sent {num_packets} packets.")
    print(f"Elapsed time: {elapsed_time:.2f} seconds.")
    print(f"Throughput: {throughput:.2f} Mbps.")