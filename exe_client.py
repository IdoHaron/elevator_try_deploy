# Import modules
from __future__ import annotations
import requests
import base64
from PIL import Image, ImageTk

import tkinter as tk
import time
import threading

# Define global variables
class CurrentTkinterState:
    image_data = None # To store the current image data
    window_closed = False # To indicate if the window is closed or not
    instance:CurrentTkinterState = None
    def __init__(self):
        self.window:tk.Tk = None
        self.label:tk.Label = None
        self.start()
        CurrentTkinterState.instance = self
    def start(self):
        self.window = tk.Tk()
        self.label = tk.Label(self.window)
        self.window.attributes("-fullscreen", True)
        self.window.overrideredirect(True)

    def update_image(self, image:tk.PhotoImage):
        self.label.config(image=image)

# Define a function that fetches and decodes the image data from the server

CurrentTkinterState()

class ManageImage:
    web_path = "https://elevator5.onrender.com/image/elevator/example"
    encoding_format = "data:image/png;base64,"
    image_data = None
    need_update = False

    @staticmethod
    def fetch_image():
        global image_data # Use the global variable
        try:
            # Fetch and decode image data
            response = requests.get(ManageImage.web_path)
            byte_string = response.content[len(ManageImage.encoding_format):] # Remove the encoding format prefix
            binary_data = base64.b64decode(byte_string)
            # Assign binary data to global variable
            ManageImage.image_data = binary_data
            ManageImage.need_update = True
        except requests.exceptions.ConnectionError:
            # Print a message if connection error occurs
            ManageImage.need_update = False

        # here you should update the screen.

# Define a function that creates a new thread to run the update function every 5 seconds

def update_image():
    ManageImage.fetch_image()
    print(1)
    if not ManageImage.need_update:
        return
    image = Image.open(ManageImage.image_data)
    CurrentTkinterState.instance.update_image(ImageTk.PhotoImage(image))

def update_thread():
    while not CurrentTkinterState.window_closed: # Check if window is still open
        # Create a new thread to run the update function
        timer = threading.Timer(5, update_image)
        timer.start() # Start the thread
        timer.join() # Wait for the thread to finish

# Open image from binary data


# Create tkinter window and label

# Convert PIL image to tkinter photo image

# Set window to full screen mode and remove title bar and borders

# Define a callback function that sets the global flag to False when window is closed
def on_closing():
    global window_closed # Use the global flag
    window_closed = True # Set flag to False

# Set window protocol to call the callback function when window is closed
CurrentTkinterState.instance.window.protocol("WM_DELETE_WINDOW", on_closing)

CurrentTkinterState.instance.window.after(5000, update_thread)
# Start main loop
CurrentTkinterState.instance.window.mainloop()
