import docker
import requests
import json
import time

API_ENDPOINT = "http://localhost:8000/scan"

def clear_log_file():
    with open("image_log.json", "w") as f:
        json.dump([], f)

def scan_all_images():
    client = docker.from_env()
    images = client.images.list()

    for image in images:
        for tag in image.tags:
            if tag:  # Skip untagged images
                print(f"Scanning image: {tag}")
                payload = {"image_tag": tag}  # Send the image tag as JSON in the body
                try:
                    response = requests.post(API_ENDPOINT, json=payload)  # Send the payload as JSON
                    if response.status_code == 200:
                        print(f"✓ Logged: {tag}")
                    else:
                        print(f"✗ Failed to log: {tag}, Error: {response.text}")
                except Exception as e:
                    print(f"✗ Exception while logging: {tag}, Error: {str(e)}")

def main():
    clear_log_file()
    scan_all_images()

if __name__ == "__main__":
    while True:
        main()
        print("Sleeping for 60 seconds...")
        time.sleep(60)
