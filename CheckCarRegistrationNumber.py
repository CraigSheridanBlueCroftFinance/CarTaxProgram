import requests
import sys

def CheckLicencePlate(NumberPlate):

    URL='https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles'
    APIKey="ot0DRUnu8N10hx6bPXQPe62UiTRtarS59ohoJaCh"

    headers = {
        'x-api-key': APIKey,
    }

    json_data = {
        'registrationNumber': NumberPlate,
    }

    response = requests.post(
        url=URL,
        headers=headers,
        json=json_data,
    )

    response=response.json()
    return response


if __name__ == '__main__':
    NumberPlate=sys.argv[1]
    MyResponse= CheckLicencePlate(NumberPlate)
    #I NEED TO PRINT THE RETURNED OBJECT IN ORDER TO RETURN IT TO EXCEL
    print("MY RESPONSE: ", MyResponse)