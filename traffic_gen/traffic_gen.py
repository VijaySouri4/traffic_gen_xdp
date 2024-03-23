# from scapy.all import *
# import time

# def send_traffic(dst_mac, interface):
#     packet = Ether(dst=dst_mac) / TCP(dport=80)
#     pkt_count = 0
#     start_time = time.time()

#     while True:
#         sendp(packet, iface=interface, verbose=False)
#         pkt_count += 1

#         if pkt_count % 1000 == 0:
#             duration = time.time() - start_time
#             throughput = pkt_count / duration
#             print(f"Sent {pkt_count} packets in {duration:.2f} seconds. Throughput: {throughput:.2f} packets/sec")

# if __name__ == '__main__':
#     # dst_ip = '10.10.1.1'  # IP address of the target machine
#     dst_mac = 'a0:36:9f:2a:5c:38'  # MAC address of the target machine
#     interface = 'enp3s0f0'  # Interface name on the source machine
#     send_traffic(dst_mac, interface)

from scapy.all import *
import time

def send_traffic(src_ip, dst_ip, src_port, dst_port, dst_mac, interface):
    packet = Ether(dst=dst_mac) / IP(src=src_ip, dst=dst_ip) / TCP(sport=src_port, dport=dst_port)
    pkt_count = 0
    start_time = time.time()

    while True:
        sendp(packet, iface=interface, verbose=False)
        pkt_count += 1

        if pkt_count % 1000 == 0:
            duration = time.time() - start_time
            throughput = pkt_count / duration
            print(f"Sent {pkt_count} packets in {duration:.2f} seconds. Throughput: {throughput:.2f} packets/sec")

if __name__ == '__main__':
    src_ip = '10.10.1.2'     # Source IP address
    dst_ip = '10.10.1.1'     # Destination IP address
    src_port = 12345         # Source port
    dst_port = 80            # Destination port
    dst_mac = 'a0:36:9f:2a:5c:38'  # MAC address of the target machine
    interface = 'enp3s0f0'   # Interface name on the source machine

    send_traffic(src_ip, dst_ip, src_port, dst_port, dst_mac, interface)