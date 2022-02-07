# Port Scanning
# todo - make dns resolution so users can input named servers
# todo - make ipv6 compatibility

# import libraries
import sys
import socket as sk
from datetime import datetime

# print welcome menu
print("=" * 50)
print("Python Port Scanner\n")
print("Only input valid IPv4 Addresses")
print("=" * 50)

# query user for ip address, todo: sanitize input
target = input("Enter IP address: ")

# Make banner based off ip-to-scan && date/time
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning Target at: " + str(datetime.now()))
print("-" * 50)

# Perform the scans and return the open ports
try:
    # Scan ports in fixed range, todo: allow user to determine range
    for port in range(1, 65535):
        s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        sk.setdefaulttimeout(1)

        # Output open ports
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

# Clean exceptions
except KeyboardInterrupt:
    print("\nExiting Program")
    sys.exit()

except sk.gaierror:
    print("\nHostname could not be resolved")
    sys.exit()

except sk.error:
    print("\nServer not responding")
    sys.exit()
