import socket
print('.########...#######..########..########.########..####.##....##..######.. ')
print(' .##.....##.##.....##.##.....##....##....##.....##..##..###...##.##....##. ')
print(' .##.....##.##.....##.##.....##....##....##.....##..##..####..##.##....... ')
print(' .########..##.....##.########.....##....########...##..##.##.##.##...#### ')
print(' .##........##.....##.##...##......##....##.........##..##..####.##....##. ')
print(' .##........##.....##.##....##.....##....##.........##..##...###.##....##. ')
print(' .##.........#######..##.....##....##....##........####.##....##..######. ')

mass = [8, 10, 12, 20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138, 139, 143, 145, 161, 179, 443, 445, 514, 515, 993, 995, 1080, 1194, 1433, 1702, 1723, 3128, 3268, 3306, 3389, 5432, 5060, 5900, 5938, 8080, 10000, 20000]
host = (str(input("Enter here IP or domain's name: ")))
print ("Please, wait...")
print ('Your name: ', socket.gethostname())
print ('Your hostname IP', socket.gethostbyname(socket.gethostname()))
print ('Your IP:', socket.gethostbyname(socket.getfqdn()))
for port in mass:
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((host,port))
    except socket.error:
        pass
    else:
        s.close
        print (host + ': port ' + str(port) + ' opened')
print ('Scanning completed')
print ("Thank you for using")
