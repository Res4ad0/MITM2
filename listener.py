import scapy.all as scapy
from scapy_http import http
import optparse

def user_network():
     parse_object = optparse.OptionParser()
     parse_object.add_option("-i","--interface",dest="interface",help="Enter your Interface")


def listen_packets(interface):
    scapy.sniff(iface="eth0",store=False,prn=analyse_packets)
    #prn = callback function

def analyse_packets(packet):
    packet.show()

listen_packets(interface)