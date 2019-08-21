import tkinter as tk
from PIL import ImageTk, Image
import requests

def get_weather(city, key):
    if city == "":
        label["text"] = "Please insert a City!"
        return
    params = {"appid": key, "q": city, "units": "metric"}
    url = r"http://api.openweathermap.org/data/2.5/weather"
    answer_json = requests.get(url, params)
    answer_json = answer_json.json()
    name = answer_json["name"]
    country = answer_json["sys"]["country"]
    description = answer_json["weather"][0]["description"]
    temp = round(float(answer_json["main"]["temp"]), 1)
    humidity = answer_json["main"]["humidity"]
    label["text"] = name +", "+ country + "\nConditions: " + description \
                    + "\nTemperature: " + str(temp) +"°C\nHumidity: " \
                    + str(humidity)


API_KEY = r""
HEIGHT = 400
WIDTH = 300

root = tk.Tk()
root.title("Tcl/Tk Weather demo")
root.resizable(False, False)
root.geometry(str(HEIGHT) + "x" + str(WIDTH))

image = Image.open("bg_weather.jpg")
bg_image = ImageTk.PhotoImage(image)
bg_label = tk.Label(root, image = bg_image)
bg_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#f3bbd4")
frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.1, anchor="n")

entry = tk.Entry(frame)
entry.place(rely= 0.10, relx=0.01, relwidth=0.6, relheight=0.8)

button = tk.Button(frame, text="Search", command=lambda: get_weather(entry.get(), API_KEY))
button.place(rely = 0.10, relx=0.65, relwidth=0.32, relheight=0.8)

lower_frame = tk.Frame(root, bg="#dabbf3")
lower_frame.place(anchor="s", relx=0.5, rely=0.9, relwidth=0.8, relheight=0.6)

label = tk.Label(lower_frame, text="Insert a city and press search...", bg="#d4f3bb", fg="black")
label.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

root.mainloop()
