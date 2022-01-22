import socket as s
import well_known as w
import process

result_arr = []
ip_arr = []
count = int(input("Ile adresów chcesz zeskanować?: "))
for i in range(count):
    print("Wprowadz adres ip nr",  i+1, end='')
    ips = input(", ktory chcesz zeskanowac:")
    ip_arr.append(ips)

for ip in ip_arr:
    # ports_range = range(1, 65535)

    while ip != 0:
        open_ports = []

        def check(ip, port, result=1):
            sock = s.socket(s.AF_INET, s.SOCK_STREAM)
            sock.settimeout(0.5)
            res = sock.connect_ex((ip, port))
            if res == 0:
                result = res
            sock.close()
            return result

        print("Processing...")

        for port in range(1, 65536):  # o jeden wiecej zeby dobic do pelnej puli
            process.timer(port)
            is_opened = check(ip, port)
            if is_opened == 0:
                open_ports.append(port)

        if len(open_ports) > 0:
            sorted(open_ports)
            w.list_well_known(open_ports, ip)

        else:
            print("Nie jestem w stanie znalezc zadnych otwartych portow...")

        cont = input("Wciśnij klawisz aby kontynuować (0 aby przerwać skanowanie):")
        if cont == 0:
            break
        else:
            continue

for i in range(count):
    print("Otwarte porty przypisane do adresu ", ip_arr[i], ": ", sep='')
    print(result_arr[i])

print("Koniec skanowania")