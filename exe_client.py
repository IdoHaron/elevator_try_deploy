# Import requests, base64, and PIL libraries
import requests
import base64
import time
from PIL import Image

# Define the URL of the server
url = "https://elevator5.onrender.com/image/elevator/example"

# Define the interval for requesting a new image in seconds
interval = 10

# Create a loop to request a new image every interval
while True:
    # Make a GET request to get the image from the server in base64 encoding
    response = requests.get(url)

    # Check the status code of the response
    if response.status_code == 200:
        # Get the base64 string from the response
        b64string = response.text
        # Decode the base64 string to bytes
        b64bytes = base64.b64decode(b64string).decode("ASCII")
        # Create an image object from the bytes
        image = Image.open(b64bytes)
        # Display the image
        image.show()
    else:
        # Print the error message
        print(f"Error: {response.status_code}")

    # Wait for the interval before requesting a new image
    time.sleep(interval)
