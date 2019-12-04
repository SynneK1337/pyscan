import scanner
import argparse

if __name__ == "__main__":
    argparser = argparse.ArgumentParser(prog="pyscan",
                                        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    argparser.add_argument('hostname', type=str, help="Hostname or ip address of host you want to scan")
    argparser.add_argument('port', type=int, help="Port you want to scan")
    argparser.add_argument('-ipv6', help="Scan IPv6 instead of IPv4", action='store_true')
    args = argparser.parse_args()

    if not args.ipv6:
        result = scanner.scan_ipv4_tcp(args.hostname, args.port)
        if result:
            print(f"[+] {args.hostname}:{args.port}/udp is open.")
        elif result is False:
            print(f"[-] {args.hostname}:{args.port}/udp is closed.")
        else:
            print(f"[!] {args.hostname} is inaccessible.")

    else:
        result = scanner.scan_ipv6_tcp(args.hostname, args.port)
        if result:
            print(f"[+] {args.hostname}:{args.port}/udp is open.")
        elif result is False:
            print(f"[-] {args.hostname}:{args.port}/udp is closed.")
        else:
            print(f"[!] {args.hostname} is inaccessible.")
