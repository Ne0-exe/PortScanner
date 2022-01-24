import socket as s


def check(ip, port):
    sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    sock.settimeout(0.5)
    res = sock.connect_ex((ip, port))
    if res == 0:
        result = res
    else:
        result = 1
    sock.close()
    return result