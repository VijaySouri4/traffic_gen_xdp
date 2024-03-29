# from scapy.all import *
# import time

# def send_traffic(dst_mac, interface):
#     packet = Ether(dst=dst_mac) / TCP(dport=80)
#     pkt_count = 0llo

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

def send_traffic(packet):
    # packet.load = _payload_
    pkt_count = 0
    start_time = time.time()

    while True:
        sendp(packet, iface=interface, verbose=False)
        pkt_count += 1

        if pkt_count % 1000 == 0:
            duration = time.time() - start_time
            throughput = pkt_count / duration
            print(f"Sent {pkt_count} packets in {duration:.2f} seconds. Throughput: {throughput:.2f} packets/sec")
            break

# if __name__ == '__main__':
#     src_ip = '10.10.1.2'     # Source IP address
#     dst_ip = '10.10.1.1'     # Destination IP address
#     src_port = 12345         # Source port
#     dst_port = 80            # Destination port
#     dst_mac = 'a0:36:9f:2a:5c:38'  # MAC address of the target machine
#     interface = 'enp3s0f0'   # Interface name on the source machine
#     _payload_ = 'Hello!'
#     num_packets = 2001
    
#     packet = Ether(dst=dst_mac) / IP(src=src_ip, dst=dst_ip) / TCP(sport=src_port, dport=dst_port) / Raw(load=_payload_)
#     packet_size = len(packet)

#     start_time = time.time()
#     # sendp(packet, count=num_packets, iface=interface, verbose=False)
#     scapy.sendrecv.sendpfast(packet, pps=1000, iface=interface, loop = num_packets, parse_results=1)
#     end_time = time.time()
    
#     # sendpfast()

#     elapsed_time = end_time - start_time
#     total_size = num_packets * packet_size
#     throughput = (total_size * 8) / (elapsed_time * 1000000)  # Throughput in Mbps

#     # print(f"Sent {num_packets} packets.")
#     print(f"Elapsed time: {elapsed_time:.2f} seconds.")
#     print(f"Throughput: {throughput:.2f} Mbps.")
    # print('sent 1000 packets')
    # send_traffic(packet)


if __name__ == '__main__':
    pcap_file = '/users/vijay4/traffic_gen/pcaps/output.pcap'  # Path to your PCAP file
    dst_mac = 'a0:36:9f:2a:5c:38'  # MAC address of the target machine
    interface = 'enp3s0f0'  # Interface name on the source machine
    src_ip = '10.10.1.2'     # Source IP address
    dst_ip = '10.10.1.1'     # Destination IP address
    src_port = 12345         # Source port
    dst_port = 80            # Destination port
    # dst_mac = 'a0:36:9f:2a:5c:38'  # MAC address of the target machine
    # interface = 'enp3s0f0'   # Interface name on the source machine
    _payload_ = 'Hello!'

    packets = rdpcap(pcap_file)
    num_packets = len(packets)
    
    print(num_packets)
    
    print("using pcap")
    
    # for i in range(0, num_packets):
    #     sendp(packets[i], iface=interface)

    start_time = time.time()

    scapy.sendrecv.sendpfast(packets, iface=interface, loop=1, parse_results=1)

    end_time = time.time()
    
    # print("using scapy generated packet")
    
    # packet = Ether(dst=dst_mac) / IP(src=src_ip, dst=dst_ip) / TCP(sport=src_port, dport=dst_port) / Raw(load=_payload_)
    
    # scapy.sendrecv.sendpfast(packet, pps=1000, iface=interface, loop = num_packets, parse_results=1)
    
    elapsed_time = end_time - start_time

    total_size = sum(len(p) for p in packets)

    throughput = (total_size * 8) / (elapsed_time * 1000000)  # Throughput in Mbps

    print(f"Sent {num_packets} packets.")
    print(f"Elapsed time: {elapsed_time:.2f} seconds.")
    print(f"Throughput: {throughput:.2f} Mbps.")
    print("end")
    
# Notes
# Make scapy send at throuhput 1000 at least 
# Measure the time at segments 1 2 and 3 from the photo
# compare user space only prog and perf 
# In the call back for the perf poll capture data at three points start of call back, start of hs, end of hs, end of call back. 
# To realise the data, understand the difference between time for each packet, difference between hs start and end for the smae oacket, differnecc efor the whole call back for the same packet. 
# Also create an experiment without the file io for hs callback. 