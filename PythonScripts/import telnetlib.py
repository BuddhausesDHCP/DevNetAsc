import telnetlib

# Connection details (replace with your test info)
HOST = "192.168.1.1"
USER = "admin"
PASSWORD = "cisco"

# Connect to the switch
tn = telnetlib.Telnet(HOST)

# Login
tn.read_until(b"Username:")
tn.write(USER.encode('ascii') + b"\n")

tn.read_until(b"Password:")
tn.write(PASSWORD.encode('ascii') + b"\n")

# Send a simple command
tn.write(b"enable\n")
tn.write(PASSWORD.encode('ascii') + b"\n")  # if enable password is the same
tn.write(b"show version\n")
tn.write(b"exit\n")

# Print the output
print(tn.read_all().decode('ascii'))
