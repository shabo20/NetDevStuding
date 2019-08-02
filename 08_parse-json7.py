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

    language = "ru_RU"
    
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest, "locale":language})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0 :
        print("API status: " + str(json_status) + " = A successfull call.\n")

        print("Directons from  " + orig + " to " + dest)
        print("Trip Duration:  " + str(json_data["route"]["formattedTime"]))
        print("Kilomiters:     " + str("{:.2f}".format(json_data["route"]["distance"]*1.61)))
        print("Fuel Used (Ltr) " + str("{:.2f}".format(json_data["route"]["fuelUsed"]*3.78)))
        print("==================================================")

        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")

    elif json_status == 402:
        print("\n******************************************************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("**********************************************************************************\n")
    
