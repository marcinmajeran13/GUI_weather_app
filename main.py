import tkinter as tk
from tkinter import font
import requests

HEIGHT = 400
WIDTH = 711


def get_weather(city):
    weather_key = '22a3d325b85ab5c074d4121436a85ffc'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


def format_response(weather):
    try:
        response = f"City: {weather['name']}\n" \
                   f"Country: {weather['sys']['country']}\n" \
                   f"Conditions: {weather['weather'][0]['description']}\n" \
                   f"Temperature: {weather['main']['temp']}°C"
    except:
        print('There was a problem retrieving this information!')
    return response



root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='backgrd.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='sea green', bd=5)
frame.place(relx=0.5, rely=0.1,  relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 20))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text='Get weather', font=('Courier', 10), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='sea green', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 20), justify='left', anchor='nw')
label.place(relwidth=1, relheight=1)

root.iconbitmap('favicon.ico')

root.title('WeatherApp')

root.mainloop()
