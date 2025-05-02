def get_images_from_unsplash(search_term, count, base_directory):
	# default data
	api_key = "Zak3UErMUP3a80OKvPO4WTCEGWOx4QN6bHi-chVShUM"
	search_url = "https://api.unsplash.com/search/photos"
	headers = {"Authorization": f"Client-ID {api_key}"}
	params = {"query": search_term, "per_page": count}

	# http request -> response
	response = requests.get(search_url, headers=headers, params=params).json()

	for i in range(count):
		image_save_path = f"{base_directory}/image{i}.jpg"
		image_url = response.get("results")[i].get("urls").get("regular")
		image_response = requests.get(image_url)

		if image_response.status_code == 200:
			with open(image_save_path, "wb") as file:
				file.write(image_response.content)
				print("Image downloaded successfully.")
		else:
			print("Failed to download the image.")


get_images_from_unsplash("mountains", 5, "/home/joncorv/Pictures/unsplash_images")