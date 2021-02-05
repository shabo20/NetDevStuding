# Entering the following code to import the requests, json, tabulate, and the functions
# from my_apic_em_functions

import requests
import json
from tabulate import*
from my_apic_em_functions import *

def print_devices():
    # Creating the variable api_url and assign a string containing the URI of the APIC-EM /host endpoint.
    # The URL is https://{YOUR-APICEM}.cisco.com/api/v1/host.
    api_url = "https://devnetsbx-netacad-apicem-1.cisco.com/api/v1/network-device"
    # Creating the variable ticket and assign to it the value returned by the get_ticket() function.
    ticket = get_ticket()
    # Creating the headers dictionary and assign it to the headers variable.
    headers = {
        "content-type": "application/json",
        "X-Auth-Token": ticket
        }
    # Creating a variable named resp, and assign to it the results of request. We use the get() method
    # to make the request by supplying it with the URL and headers variables created above
    resp = requests.get(api_url, headers=headers, verify=False)
    # Printing status of the request
    print("Status of /host request: ", resp.status_code)
    # Create an if condition to detect if the status code returned by the API is anything other than 200.
    # If this condition was true, the request was unsuccessful. If the request fails, raise an exception
    # and provide the error message as shown in the code block below.
    if resp.status_code != 200:
        raise Exception("Status code does not equal 200. Response text: " + resp.text)
    # Creating a variable to hold the response JSON that has been converted to Python dictionary format.
    response_json = resp.json()
    # In this step, we will create a for loop to parse the JSON data and create a table.
    device_list = []
    i = 0
    for item in response_json["response"]:
        i+=1
        device = [
            i,
            item["series"],
            item["managementIpAddress"]
            ]
        device_list.append( device )
        table_header = ["Number", "Type", "IP"]
    print( tabulate(device_list, table_header) )
