# Port Scanner with functions to allow for IPv4/IPv6 scanning as well as named targets(dns)
# todo: Add IPv6 functionality, Add Name Resolution

# import libraries
import sys
import socket as sk
from datetime import datetime

# Scans IPv4 addresses with user-defined port range
def scan_ip4(low_port, high_port):

    # Set target ipv4, todo: sanitize input
    target = input("Enter the IPv4 address to scan: ")

    # Make banner based off ip-to-scan && date/time
    print("-" * 50)
    print("Scanning Target: " + target)
    print("Scanning Target at: " + str(datetime.now()))
    print("-" * 50)

    try:

        # Scans ports in user defined range
        for port in range(low_port, high_port):
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


def scan_ip6(low_port, high_port):
    print("You made it to scanning ipv6!")
    print(low_port, high_port)


def scan_name(low_port, high_port):
    print("You made it to scanning name!")
    print(low_port, high_port)


def main():
    
    # todo: Make welcome menu (find replacement of pyfiglet)
    
    print("Are you scanning: (1)IPv4, (2)IPv6, (3)Public Hostname")
    scan_type = input("Please choose, [1, 2, or 3]: ")

    low_port = input("Enter first port to start scanning: ")
    high_port = input("Enter last port to finish scanning: ")
    
    # Determine which function to goto next
    if scan_type == "1":
        scan_ip4(low_port, high_port)
    elif scan_type == "2":
        scan_ip6(low_port, high_port)
    else:
        scan_name(low_port, high_port)


main()
