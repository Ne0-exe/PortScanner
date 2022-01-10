import socket as s

ip = '192.168.0.1'
open_ports = []
#ports_range = range(1, 65535)

def check (ip, port, result = 1):
    # TRY:
    sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    sock.settimeout(0.5)
    res = sock.connect_ex((ip, port))
    if res == 0:
        result = res
    sock.close()
    #EXCEPT EXCEPTION AS EX:
    #   PASS
    return result

for port in range(1, 65536):  # o jeden wiecej zeby dobic do pelnej puli
    is_opened = check(ip, port)
    if is_opened == 0:
        open_ports.append(port)

if len(open_ports) > 0:
    print("Oto otwarte porty:\n", sorted(open_ports))
else:
    print("Nie jestem w stanie znalezc zadnych otwartych portow...")

    #OUTPUT:

    # Oto otwarte porty:
    # [53, 80, 5000]
