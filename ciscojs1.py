import telnetlib
import json

with open('cisco1.json') as f:
    data = json.load(f)

for entry in data['router']:
    host_ip = entry['host_ip']
    username = entry['username']
    password = entry['password']
    hostname = entry['hostname']

    tn = telnetlib.Telnet(host_ip)

    tn.read_until(b"Username: ")
    tn.write(username.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"enable\n")
    tn.write(b"pass\n")
    tn.write(b"conf t\n")
    tn.write(b"hostname " + hostname.encode('ascii') + b"\n")

    lo_number = 1
    for interface in entry['lo_interfaces']:
        tn.write(b"no int lo " + str(lo_number).encode('ascii') + b"\n")
        tn.write(b"int lo" + str(lo_number).encode('ascii') + b"\n")
        tn.write(b"ip add " + interface.encode('ascii') + b" 255.255.255.0\n")
        tn.write(b"no shut\n")
        lo_number = lo_number + 1

    tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
    tn.close()

f.close()
