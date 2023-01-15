import telnetlib

HOST = "localhost"
PORT=2601
user = 'zebra'
password = ''

tn = telnetlib.Telnet(HOST,PORT)

tn.read_until(b"Password: ")
tn.write(user.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.read_until(b"Password: ")
tn.write(user.encode('ascii') + b"\n")
tn.write(b"show startup-config\n")
tn.write(b"quit\n")

print(tn.read_all().decode('ascii'))

