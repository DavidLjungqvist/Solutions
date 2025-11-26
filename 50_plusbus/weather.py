import httpx  # pip install httpx
import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

KEY = "2a3891ce1248786a1398a888debb0368"  # ulsc@aspit.dk


def weather_now(city, key=KEY):
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&APPID=" + key
    response = httpx.get(url)
    weather = response.json()  # Deserialize json into a hierarchy of dictionaries and lists

    if weather["cod"] == "404":
        return "Unknown Location"

    print(f'{weather=}')
    print(f'{weather["weather"]=}')
    print(f'{weather["weather"][0]["main"]=}')
    print(f'{int(weather["main"]["temp"])=}')
    if weather["cod"] == 200:
        weather_report = city + ": " + weather["weather"][0]["main"] + ", " + str(int(weather["main"]["temp"])) + "°C"
    else:
        weather_report = "Unknown Location"
    return weather_report

def get_weather_icon(icon_code):
    url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"

    response = requests.get(url)
    image_data = response.content

    pil_image = Image.open(BytesIO(image_data))
    tk_image = ImageTk.PhotoImage(pil_image)

    return tk_image

def get_icon_code(city, key=KEY):
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&APPID=" + key
    response = httpx.get(url)
    weather = response.json()  # Deserialize json into a hierarchy of dictionaries and lists


    if weather["cod"] == 200:
        weather_icon = weather["weather"][0]["icon"]
    else:
        weather_icon = "Unknown icon"
    return weather_icon


def main(city, KEY):

    root = tk.Tk()
    root.title("Weather Icon")
    root.configure(bg="#1e1e1e")

    print(weather_now(city, KEY))

    icon_code = get_icon_code(city, KEY)

    icon_img = get_weather_icon(icon_code)

    label = tk.Label(root, image=icon_img, bg="#0e0e0e")
    label.image = icon_img
    label.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":  # Executed when invoked directly
   main("los angeles", KEY)
