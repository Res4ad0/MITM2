import scapy.all as scapy
import optparse

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ipadress",dest="ip_adress",help="Enter yOUR IP")
    (user_input,arguments) = parse_object.parse_args()
    if not user_input.ip_adress:
        print("enter yOUR IP,bitch")
    return user_input
def scan_my_ip(ip):
    arp_request_packet = scapy.ARP(pdst="ip")
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet=broadcast_packet/arp_request_packet
    (answered_list,unanswered_list)=scapy.srp(combined_packet,timeout=1)
    answered_list.summary()

user_ip_adress = get_user_input()
scan_my_ip(user_ip_adress.ip_adress)