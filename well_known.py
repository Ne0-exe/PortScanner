
def list_well_known(open_ports, ip):
    for i in range(len(open_ports)):
        if (open_ports[i] == 20) or (open_ports[i] == 21):
            print('[', open_ports[i], "] : FTP service is open")
        elif open_ports[i] == 22:
            print('[', open_ports[i], "] : SSH/SFTP service is open")
        elif open_ports[i] == 23:
            print('[', open_ports[i], "] : Telnet service is open")
        elif open_ports[i] == 25:
            print('[', open_ports[i], "] : SMTP service is open")
        elif open_ports[i] == 53:
            print('[', open_ports[i], "] : DNS service is open")
        elif (open_ports[i] == 67) or (open_ports[i] == 68):
            print('[', open_ports[i], "] : DHCP service is open")
        elif open_ports[i] == 69:
            print('[', open_ports[i], "] : TFTP service is open")
        elif open_ports[i] == 80:
            print('[', open_ports[i], "] : HTTP service is open")
        elif open_ports[i] == 110:
            print('[', open_ports[i], "] : POP3 service is open")
        elif open_ports[i] == 123:
            print('[', open_ports[i], "] : NTP service is open")
        elif open_ports[i] == 139:
            print('[', open_ports[i], "] : NetBIOS service is open")
        elif open_ports[i] == 143:
            print('[', open_ports[i], "] : IMAP service is open")
        elif (open_ports[i] == 161) or (open_ports[i] == 162):
            print('[', open_ports[i], "] : SNMP service is open")
        elif open_ports[i] == 389:
            print('[', open_ports[i], "] : LDAP service is open")
        elif open_ports[i] == 443:
            print('[', open_ports[i], "] : HTTPS service is open")
        elif open_ports[i] == 445:
            print('[', open_ports[i], "] : SMB service is open")
        elif open_ports[i] == 514:
            print('[', open_ports[i], "] : Syslog service is open")
        elif open_ports[i] == 587:
            print('[', open_ports[i], "] : SMTP TLS service is open")
        elif open_ports[i] == 636:
            print('[', open_ports[i], "] : LDAPS service is open")
        elif open_ports[i] == 993:
            print('[', open_ports[i], "] : IMAP SSL service is open")
        elif open_ports[i] == 995:
            print('[', open_ports[i], "] : POP3 SSL service is open")
        elif open_ports[i] == 1433:
            print('[', open_ports[i], "] : SQL service is open")
        elif open_ports[i] == 1521:
            print('[', open_ports[i], "] : SQLnet service is open")
        elif open_ports[i] == 3306:
            print('[', open_ports[i], "] : MySQL service is open")
        elif open_ports[i] == 3389:
            print('[', open_ports[i], "] : RDP service is open")
        elif (open_ports[i] == 5060) or (open_ports[i] == 5061):
            print('[', open_ports[i], "] : SIP service is open")
        else:
            print('[', open_ports[i], "] : opened")


