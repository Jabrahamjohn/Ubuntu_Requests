import os
import requests
from urllib.parse import urlparse

def fetch_image():
    # Prompt the user for an image URL
    image_url = input("Enter the URL of the image: ")

    # Create the "Fetched_Images" directory if it doesn't exist
    directory = "Fetched_Images"
    os.makedirs(directory, exist_ok=True)

    try:
        # Send a GET request to fetch the image
        response = requests.get(image_url, stream=True)
        response.raise_for_status()  # Check for HTTP errors

        # Extract the filename from the URL
        parsed_url = urlparse(image_url)
        filename = os.path.basename(parsed_url.path) or "downloaded_image"

        # Save the image in binary mode
        file_path = os.path.join(directory, filename)
        with open(file_path, "wb") as image_file:
            for chunk in response.iter_content(chunk_size=8192):
                image_file.write(chunk)

        print(f"Image successfully downloaded and saved as: {file_path}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the image: {e}")

if __name__ == "__main__":
    fetch_image()