import datetime

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium

def get_number():
    while True:
        try:
            number = input("Enter phone number with country code: ")
            check_number = phonenumbers.parse(number)
            if phonenumbers.is_valid_number(check_number):
                return number
            else:
                print("Invalid phone number. Please try again.")
        except phonenumbers.NumberParseException:
            print("Invalid phone number format. Please try again.")

def get_location_info(number):
    number_location = geocoder.description_for_number(phonenumbers.parse(number), "en")
    service_provider = phonenumbers.parse(number)
    provider_name = carrier.name_for_number(service_provider, "en")
    return number_location, provider_name

def get_coordinates(location):
    results = opencage_geocoder.geocode(location)
    if results and 'geometry' in results[0]:
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        return lat, lng
    else:
        print("Error fetching coordinates.")
        return None, None

def main():
    number = get_number()

    number_location, provider_name = get_location_info(number)
    print(f"Location: {number_location}")
    print(f"Service Provider: {provider_name}")

    lat, lng = get_coordinates(str(number_location))
    if lat is not None and lng is not None:
        print(f"Latitude: {lat}, Longitude: {lng}")

        # Format the current date for the HTML file name
        current_date = datetime.datetime.now().strftime("%d-%b-%Y")
        html_file_name = f"contact_info_{current_date}.html"

        map_location = folium.Map(location=[lat, lng], zoom_start=9)
        folium.Marker([lat, lng], popup=f"{number_location}<br>{provider_name}").add_to(map_location)

        map_location.save(html_file_name)
        print(f"Map saved as {html_file_name}")
    else:
        print("Map generation failed.")


if __name__ == "__main__":
    opencage_geocoder = OpenCageGeocode("6d6f969fd9024ac8afde957f0c86a5ba")  # Replace with your actual OpenCage API key
    main()
