import googlemaps
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLEMAPS_API = os.environ.get('GOOGLEMAPS_API')

def getgps(location, keyword):
    google_maps = googlemaps.Client(GOOGLEMAPS_API)
    geocode_result = google_maps.geocode((f"{location} {keyword}"))

    latitude = geocode_result[0]['geometry']['location']['lat']
    longitude = geocode_result[0]['geometry']['location']['lng']

    return f"{location} {keyword} : {latitude}, {longitude}"


print(getgps('komodo', 'castlerock'))