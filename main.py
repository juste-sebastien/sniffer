#!usr/bin/env python3
# coding:utf8

import argparse
import sniffer


def main():
    parser = argparse.ArgumentParser(description='Sniffing network tool')
    parser.add_argument(
        '-iface',
        dest='iface',
        help='Network interface to use',
        required=False
    )

    args = parser.parse_args()

    if args.iface:
        sniffer.sniffer(args.iface)


if __name__ == '__main__':
    main()
