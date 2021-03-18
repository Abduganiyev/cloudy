
from pyowm import OWM
import ctypes
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
import colorama
from colorama import Fore, Back, Style
colorama.init()
# ---------- FREE API KEY examples ---------------------
while True:
		
	city = input("which city you are interested in: ")
	owm = OWM('6d00d1d4e704068d70191bad2673e0cc')
	mgr = owm.weather_manager()


	observation = mgr.weather_at_place(city)
	w = observation.weather
	Temp_min = w.temperature('celsius')['temp_min']
	Temp_now = w.temperature('celsius')['temp']
	Temp_max = w.temperature('celsius')['temp_max']
	Humidity = w.humidity
	Detailed_status = w.detailed_status
	print(Back.WHITE + Fore.RED + "In the " + city + " temp. min is " + str(Temp_min) + "°C" + ", temp. now is " + str(Temp_now) + "°C" + ", temp. max is " + str(Temp_max) + "°C" + ", status is " + Detailed_status + ", humidity is " + str(Humidity) + "%" )
	print(Style.RESET_ALL)