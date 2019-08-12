import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "Lcn00Cv15yjonJADd1R58bncw7zR2c88"

while True:
    orig = input ("Starting location: ")
    if orig == "quit" or orig == "q":
        break
    
    dest = input ("Destination : ")
    if dest == "quit" or dest == "q":
        break

    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0 :
        print("API status: " + str(json_status) + " = A successfull call.\n")

