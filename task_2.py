import socket
import sys
import threading
import time
from datetime import datetime

import pyfiglet
import requests


def chose_option():
    print("-"*50)
    print("\t1. Port Scan For IP .\n\t2. Vulnerability Scan For Website.\n\t3. Exit Program.")
    print("-"*50)
    user_choice = int(input("Choose Option : "))
    match user_choice:
        case 1:
            # Banner
            print(pyfiglet.figlet_format("RAHUKALSH'S PORT SCANNER"))
            ip_add = input("Please Enter Target IP Address : ")
            print("-"*50)
            print("Scanning Target: " + ip_add)
            print("Scanning Started At: " + str(datetime.now()))
            print("-"*50)
            start_time = time.time()

            #### ------------------------- Without Using Threading Method ----------------------
            # try:
            #     for i in range(1, 100):
            #         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #         socket.setdefaulttimeout(2)
            #         connect = s.connect_ex((ip_add, i))
            #         if connect == 0:
            #             print("[*] Port {} is OPEN".format(i))
            #         s.close()
            # except KeyboardInterrupt:
            #     print("\n Exiting :(")
            #     sys.exit()
            # except socket.error:
            #     print("\n Host Not Responding :(")
            #     sys.exit()
            # -------------------------------------------------------------------------------------

            def scan_port(ip_add, port):
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket.setdefaulttimeout(2)
                    # s.settimeout(2)
                    conn = s.connect_ex((ip_add, port))
                    if(not conn):
                        print("[*] Port {} is OPEN".format(port))
                    s.close()
                except KeyboardInterrupt:
                    print("\n Exiting :(")
                    sys.exit()
                except socket.error:
                    print("\n Host Not Responding :(")
                    sys.exit()

            for i in range(1, 1000):
                t = threading.Thread(target= scan_port, args = (ip_add, i))
                t.start()

            end_time = time.time()
            print("Time elapsed :",end_time-start_time,'s')

        case 2:
            # Banner
            print(pyfiglet.figlet_format("WEB Vuln SCANNER"))
            domain = input("Enter Domain URL : ")
            print("-"*50)
            print("Scanning Target: ",domain)
            print("Scanning Started At: " + str(datetime.now()))
            print("-"*50)

            header = requests.get(domain).headers
            if "X-Frame-Options" in header:
                print(f"\n[*]  Website {domain} Contain X-Frame-Options in Header.\n[*]  Status -> Not Vulnerable.")
            else:
                print(f"\n[*]  Website {domain} does'nt Contain X-Frame-Options in Header.\n[*]  Status -> Vulnerable.\n[*]  Type -> Click-Jacking Vulnerability.")

            show_header = input("\nDo you want to see Header details of "+ domain +"\n-> Y/N : ")
            if show_header == "y" or show_header == "Y":
                print(f"This is Complete Website Header : {header}")
            elif show_header == "n" or show_header == "N":
                print("\n[-] Okay as your wish !!!")
            else:
                print("\n------ Closed --------")

        case 3:
            print("\n\tOkay Exiting....! ")
            sys.exit()

        case _:
            print("\n<---- Unknown Option Chosen ----->\n######## Choose Again #########")
            chose_option()

chose_option()
