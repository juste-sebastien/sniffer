from scapy.all import *
from scapy.layers import http


def sniffer(interface):
    """
    Try to get info of specify network
    :param interface: network
    :return:
    """
    scapy.all.sniff(
        iface=interface,
        store=False,
        prn=callback,
    )


def callback(packet):
    """
    Try to print OSI Model layers
    :param packet: network packet send by sniffer()
    :return:
    """
    if packet.haslayer(http.HTTPRequest):
        print('[*]',packet.show())

