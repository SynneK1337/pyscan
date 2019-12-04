import socket


def scan_ipv4_tcp(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except ConnectionRefusedError:
        return False
    except socket.gaierror:
        return None
    else:
        return True


def scan_ipv4_udp(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect((host, port))
    except ConnectionRefusedError:
        return False
    except socket.gaierror:
        return None
    else:
        return True


def scan_ipv6_tcp(host, port):
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except ConnectionRefusedError:
        return False
    except socket.gaierror:
        return None
    else:
        return True


def scan_ipv6_udp(host, port):
    s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    try:
        s.connect((host, port))
    except ConnectionRefusedError:
        return False
    except socket.gaierror:
        return None
    else:
        return True
