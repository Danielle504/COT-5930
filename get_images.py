from pexels_api import API
from urllib.request import Request, urlopen
import re
import os

# Insert Pexels API Key here
PEXELS_API_KEY = "Insert_API_Key"
api = API(PEXELS_API_KEY)

# Popular cat breeds
breeds = [
    "Bengel Cat",
    "Siberian Cat",
    "Persian Cat",
    "Burmese Cat",
    "Oriental Cat",
    "Himalayan Cat",
    "British Shorthair Cat",
]

for breed in breeds:
    api.search(breed, results_per_page=100)
    photos = api.get_entries()
    os.makedirs("cats/" + breed + "/", exist_ok=True)
    for photo in photos:
        # Uncomment this to print original photo link
        # print("Photo url: ", photo.original)
        # REGEX to get end of link
        pic = re.search("([^/]+)/?$", photo.original).group()
        # Saves photos
        req = Request(
            url="https://images.pexels.com/photos/20001743/pexels-photo-20001743.jpeg",
            headers={"User-Agent": "Mozilla/5.0"},
        )
        webpage = urlopen(req).read()
        output = open("cats/" + breed + "/" + pic, "wb")
        output.write(webpage)
    output.close()
