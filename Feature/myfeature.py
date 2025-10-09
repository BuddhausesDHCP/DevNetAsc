import telnetlib
import time

# Device connection details
HOST = "192.168.1.100"   # Replace with your switch/router IP
USER = "admin"           # Replace with your login username
PASSWORD = "password"    # Replace with your login password

# The trivial config change you want to make
NEW_SNMP_MANAGER_IP = "192.168.1.200"

try:
    # Open Telnet connection
    tn = telnetlib.Telnet(HOST)

    # Login
    tn.read_until(b"Username: ")
    tn.write(USER.encode('ascii') + b"\n")
    tn.read_until(b"Password: ")
    tn.write(PASSWORD.encode('ascii') + b"\n")

    # Enter configuration mode
    tn.write(b"configure terminal\n")
    time.sleep(1)

    # Update SNMP manager IP (command syntax depends on vendor!)
    tn.write(f"snmp-server host {NEW_SNMP_MANAGER_IP}\n".encode("ascii"))
    time.sleep(1)

    # Save config
    tn.write(b"write memory\n")
    time.sleep(1)

    # Exit
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))

except Exception as e:
    print(f"Connection failed: {e}")
