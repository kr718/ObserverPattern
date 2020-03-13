import WeatherStation
import PhoneWeatherService

def main():
	station = WeatherStation.WeatherStation()
	phone = PhoneWeatherService.PhoneWeatherService(station)
	station.Add(phone)
	station.Run()

if __name__ == "__main__":
	main()