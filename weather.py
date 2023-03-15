#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from PIL import Image, ImageTk
import requests

# Set your WeatherAPI API key here
API_KEY = "200453c14a9e4c1581a10543231503"

# Set up the GUI
root = Tk()
root.title("Weather App")

city_label = Label(root, text="Enter a city:")
city_label.pack()

city_entry = Entry(root)
city_entry.pack()

weather_label = Label(root, text="")
weather_label.pack()

icon_label = Label(root)
icon_label.pack()

refresh_button = Button(root, text="ARA")

# Define a function to get weather information for a given city
def get_weather():
    # Get the user's input for the city
    city = city_entry.get()
    # Make a request to the WeatherAPI API
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url).json()
    # Get the current temperature and condition from the API response
    current_temp = response["current"]["temp_c"]
    condition = response["current"]["condition"]["text"]
    # Set the weather label text
    weather_label.config(text=f"{city}: {current_temp}°C, {condition}")
    # Get the weather icon from the API response
    icon_url = f"http:{response['current']['condition']['icon']}"
    icon_response = requests.get(icon_url, stream=True)
    # Open the icon image using PIL
    img = Image.open(icon_response.raw)
    # Resize the image to 100x100 pixels and convert to PhotoImage format
    img = img.resize((100, 100), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    # Set the image on the icon label
    icon_label.config(image=photo)
    icon_label.image = photo

# Define a function to handle the Refresh button click
def handle_refresh():
    get_weather()

# Bind the Refresh button to the handle_refresh function
refresh_button.config(command=handle_refresh)
refresh_button.pack()

# Start the Tkinter event loop
root.mainloop()


# In[ ]:




