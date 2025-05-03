import requests

from pprint import pprint


# def get_images_from_pexels(search_term, count, base_directory):
# default data
api_key = "rM5ZwdZtKEgHvY7f5ux0Z26RXcyZkkaGZoKDtC5hoGvxnBRxtFPO2tJ0"
search_url = "https://api.pexels.com/v1/search"
search_term = "The Shining Mountain Snow Cabin"
base_directory = "/Users/jonncorv/Desktop/temp_photos"
count = 5
headers = {"Authorization": api_key}
params = {"query": search_term, "per_page": count}

# http request -> response
response = requests.get(search_url, headers=headers, params=params).json()

# pprint(response)

for i in range(count):
    image_save_path = f"{base_directory}/image{i}.jpg"
    image_url = response.get("photos")[i].get("src").get("medium")
    image_response = requests.get(image_url)

    if image_response.status_code == 200:
        with open(image_save_path, "wb") as file:
            file.write(image_response.content)
            print("Image downloaded successfully.")
    else:
        print("Failed to download the image.")


# get_images_from_pexels("mountains", 5, "/home/joncorv/Pictures/unsplash_images")
