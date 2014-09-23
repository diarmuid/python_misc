__author__ = 'diarmuid'

import socket
import iNetxFast

mysocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

recv_sequencenums = {}
missed_packets = {}
packet_count = 0

mysocket.bind(("127.0.0.1",8010))

while True:
    data,addr = mysocket.recvfrom(16)
    inetpacket = iNetxFast.iNetxFast(data)
    if inetpacket.streamid in recv_sequencenums:
        if not ( (( recv_sequencenums[inetpacket.streamid] + 1) % pow(2,16)) == inetpacket.sequence):
            if inetpacket.streamid in missed_packets:
                missed_packets[inetpacket.streamid] += inetpacket.sequence - ( recv_sequencenums[inetpacket.streamid] + 1) % pow(2,16)
            else:
                missed_packets[inetpacket.streamid] =  inetpacket.sequence - ( recv_sequencenums[inetpacket.streamid] + 1) % pow(2,16)
    recv_sequencenums[inetpacket.streamid] = inetpacket.sequence


    packet_count += 1

if packet_count % 1000:
    for id,seq in missed_packets.iteritems():
        print "ERROR: StreamID={:5X} LostPackets={:10d}".format(id,seq)
    for id,seq in recv_sequencenums.iteritems():
        print "INFO:  StreamID={:5X} RecvPackets={:10d}".format(id,seq)