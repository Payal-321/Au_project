#import os
#os.system('Xvfb :1 -screen 0 1600x1200x16  &')    # create virtual display with size 1600x1200 and 16 bit color. Color can be changed to 24 or 8
#os.environ['DISPLAY'] = ':1.0'    # tell X clients to use our virtual DISPLAY :1.0.

import requests
import tkinter as tk

# Fetch INR base rates from API
url = "https://open.er-api.com/v6/latest/INR"
response = requests.get(url)
response_data = response.json()

# Selected currencies to convert to/from
selected_countries = ['AED', 'ALL', 'AFN']

# Create GUI window
root = tk.Tk()
root.title("INR Exchange Rate Viewer")

# Add header label
header = tk.Label(root, text="Exchange Rates (INR Base)", font=("Helvetica", 16, "bold"))
header.pack(pady=10)

# Display rates in the GUI
for country in selected_countries:
    rate = response_data['rates'][country]
    inverse = 1 / rate
    message = f"1 INR = {rate:.4f} {country} | 1 {country} = {inverse:.4f} INR"
    label = tk.Label(root, text=message, font=("Helvetica", 12))
    label.pack(pady=5)

# Run the Tkinter event loop
root.mainloop() # Removing this line as it's not needed in Colab