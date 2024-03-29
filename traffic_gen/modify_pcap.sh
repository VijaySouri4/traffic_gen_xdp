#!bin/bash

tcprewrite --enet-dmac=a0:36:9f:2a:5c:38 --enet-smac=a0:36:9f:28:fa:20 --infile=/users/vijay4/traffic_gen/pcaps/tipc-publication-payload-withdrawal.pcap --outfile=/users/vijay4/traf
fic_gen/pcaps/output2.pcap

sudo tcpreplay -i enp3s0f0 /users/vijay4/traffic_gen/pcaps/output2.pcap 