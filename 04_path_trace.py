import requests
import json
import time

from my_apic_em_functions import *
from tabulate import *

requests.packages.urllib3.disable_warnings()

api_url = "https://devnetsbx-netacad-apicem-1.cisco.com/api/v1/flow-analysis"
ticket = get_ticket()
headers = {
        "content-type": "application/json",
        "X-Auth-Token": ticket
        }
print("\n\n")

print("List of hosts on the network: ")
print_hosts()
print("\n\n")

print("List of network devices on the network: ")
print_devices()
print("\n\n")

while True:
    s_ip = input("Please enter the source host IP address for the path trace: ")
    d_ip = input("Please enter the destination host IP address for the path trace: ")

    if s_ip != "" and d_ip != "":
        path_data = {
            "sourceIP": s_ip,
            "destIP": d_ip
            }

        print("Source IP address is: ", path_data["sourceIP"])
        print("Destination IP address is: ", path_data["destIP"])

        break


    else:
        print("\n You must enter correct IP address! \n use CTRL + c to exit \n")
        continue 
        
path = json.dumps(path_data)

resp = requests.post(api_url, path, headers=headers, verify=False)

resp_json = resp.json()

flowAnalysisID = resp_json["response"]["flowAnalysisId"]
print("Flow Analysis ID: ", flowAnalysisID)
