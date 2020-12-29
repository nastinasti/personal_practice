import tkinter as tk
import requests

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 700


def parse_data(raw_data):
	city_name = raw_data.get("name")
	city_weater_data = raw_data.get("weather", dict())
	city_weater = city_weater_data[0].get("description")
	city_temp = raw_data.get("main", dict()).get("temp")

	return f"{city_name}: {city_weater}\n{city_temp} C"


def get_data(city):
	if city == '':
		update_weather_label("You forgot to enter the city!") 
		return

	base_url = "https://api.openweathermap.org/data/2.5/weather"
	appid = "a4aa5e3d83ffefaba8c00284de6ef7c3"
	params = {"APPID": appid, "q" : city, "units": "metric"}
	response = requests.get(base_url, params=params)
	if response.status_code != 200:
		update_weather_label("Failed to get weather!")
		return

	weater_data = parse_data(response.json())
	update_weather_label(weater_data)




def update_weather_label(data):
	weather_label["text"] = data


root = tk.Tk()

main_canvas = tk.Canvas(root, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
main_canvas.pack()


top_container = tk.Frame(main_canvas, bg='#80c1ff')
top_container.place(height=250, width=450, x=25, y = 25)


bottom_container = tk.Frame(main_canvas, bg='#E5E5E5')
bottom_container.place(height=400, width=450, x=25, y=275)

search_input = tk.Entry(top_container, text="City name")
search_input.place(relwidth=0.75, height=30, relx=0.12, rely=0.1)

search_button = tk.Button(top_container, text='Get weather', command=lambda: get_data(search_input.get()))
search_button.place(relwidth=0.3, rely=0.3, relx=0.35)

weather_label = tk.Label(bottom_container, text="Weather data will be here")
weather_label.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

root.mainloop()
