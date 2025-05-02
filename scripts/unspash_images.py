import requests
import os
import json
import time


def download_unsplash_images(search_term, count, folder_path):
	"""
	Download images from Unsplash based on search term

	Parameters:
	search_term (str): Term to search for
	count (int): Number of images to download
	folder_path (str): Folder to save images to
	"""
	# Replace with your own access key from https://unsplash.com/developers
	UNSPLASH_ACCESS_KEY = "Zak3UErMUP3a80OKvPO4WTCEGWOx4QN6bHi-chVShUM"

	# Create folder if it doesn't exist
	if not os.path.exists(folder_path):
		os.makedirs(folder_path)
		print(f"Created folder: {folder_path}")

	# Search for images
	search_url = "https://api.unsplash.com/search/photos"
	headers = {"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}
	params = {"query": search_term, "per_page": count}

	response = requests.get(search_url, headers=headers, params=params)

	if response.status_code != 200:
		print(f"Error searching images: {response.status_code}")
		return

	data = response.json()
	photos = data["results"]
	print(f"Found {len(photos)} images for search term: '{search_term}'")

	# Download each image
	for i, photo in enumerate(photos):
		image_url = photo["urls"]["regular"]
		photographer = photo["user"]["name"].replace(" ", "_")
		file_name = f"{search_term}_{i + 1}_by_{photographer}.jpg"
		file_path = os.path.join(folder_path, file_name)

		print(f"Downloading image {i + 1}/{len(photos)}: {file_name}")

		# Download image
		img_response = requests.get(image_url)

		if img_response.status_code == 200:
			with open(file_path, "wb") as img_file:
				img_file.write(img_response.content)
			print(f"Saved image to: {file_path}")

			# Adding slight delay to be respectful to the API
			time.sleep(0.5)
		else:
			print(f"Failed to download image: {img_response.status_code}")

	print(f"Successfully downloaded {len(photos)} images to {folder_path}")


if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser(description="Download images from Unsplash")
	parser.add_argument("search_term", help="Term to search for")
	parser.add_argument(
		"--count", type=int, default=5, help="Number of images to download (default: 5)"
	)
	parser.add_argument(
		"--folder",
		default="./unsplash_images",
		help="Folder to save images to (default: ./unsplash_images)",
	)

	args = parser.parse_args()

	download_unsplash_images(args.search_term, args.count, args.folder)