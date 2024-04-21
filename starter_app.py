import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os
import ttkbootstrap

def search():
    selection = dropdown.get()
    if selection == "Current Location":
        run_location_based()
    elif selection == "Enter City Name":
        run_user_input_city()
    elif selection =="Air Pollution":
        run_user_air_pollution()
    elif selection =="Forecast Every 3 Hours":
        run_user_forecast()
    else:
        messagebox.showwarning("Selection Error", "Please choose an option.")

def run_user_input_city():
    script_path = os.path.join(os.path.dirname(__file__), "user_input_city.py")
    subprocess.Popen(["python", script_path])

def run_location_based():
    script_path = os.path.join(os.path.dirname(__file__), "location_based.py")
    subprocess.Popen(["python", script_path])

def run_user_air_pollution():
    script_path=os.path.join(os.path.dirname(__file__), "air_pollution.py")
    subprocess.Popen(["python",script_path])

def run_user_forecast():
    script_path=os.path.join(os.path.dirname(__file__), "forecast.py")
    subprocess.Popen(["python",script_path])

root = ttkbootstrap.Window(themename="flatly")
root.title("Weather")
root.geometry("400x400")

dropdown_label = ttkbootstrap.Label(root, text="WeatherWise", font="Bembo, 16")
dropdown_label.pack(pady=10)

options = ["Select Option", "Current Location", "Enter City Name","Air Pollution", "Forecast Every 3 Hours"]
dropdown = ttk.Combobox(root, values=options, font="Bembo, 14")
dropdown.current(0)
dropdown.pack(pady=10)

search_button = ttkbootstrap.Button(root, text="Search", command=search, bootstyle="outline warning")
search_button.pack(pady=10)

location_label = ttkbootstrap.Label(root, font="Bembo, 20")
location_label.pack(pady=20)

icon_label = ttkbootstrap.Label(root)
icon_label.pack()

temp_label = ttkbootstrap.Label(root, font="Bembo, 18")
temp_label.pack()

desc_label = ttkbootstrap.Label(root, font="Bembo, 18")
desc_label.pack()

root.mainloop()
