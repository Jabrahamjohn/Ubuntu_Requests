import requests
import os
from urllib.parse import urlparse

def main():
    # Prompt user for URL
    url = input("Enter the URL containing an image: ").strip()
    
    if not url:
        print("No URL provided. Exiting.")
        return
    
    # Create directory if it doesn't exist
    directory = "Fetched_Images"
    os.makedirs(directory, exist_ok=True)
    
    # Extract filename from URL
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    
    # If no filename or extension, generate a default one
    if not filename or '.' not in filename:
        content_type = 'image/jpeg'  # Default fallback
        try:
            response = requests.head(url, allow_redirects=True)
            response.raise_for_status()
            content_type = response.headers.get('content-type', 'image/jpeg')
        except:
            pass  # Use default if HEAD fails
        ext = content_type.split('/')[-1] if '/' in content_type else 'jpg'
        filename = f"downloaded_image.{ext}"
    
    # Full filepath
    filepath = os.path.join(directory, filename)
    
    # Download and save the image
    try:
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()
        
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"Image successfully downloaded and saved to: {filepath}")
        
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred while fetching the image: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Network error occurred while fetching the image: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()