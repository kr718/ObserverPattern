from random import *
import time
class weatherStation(object):
	"""docstring for weatherStation"""
	def __init__(self):
		super(weatherStation, self).__init__()
		self.tempreture = randint(0,32)
		self.ListOfObservers = []

	def add(self,observer):
		self.ListOfObservers.append(observer) 

	def add(self,*args):
		for arg in args:
			self.ListOfObservers.append(arg) 

	def Notify(self):
		for observer in self.ListOfObservers:
			observer.update()

	def GetWeather(self):
		return self.tempreture

	def Run(self):
		while True:
			time.sleep(1)
			self.tempreture = randint(10,32)
			self.Notify()
		

class PhoneWeatherService(object):
	def __init__(self,station):
		self.station = station

	def update(self):
		print ("Weather on Phone is:" + str(self.station.GetWeather()))

class WebsiteWeatherService(object):
	def __init__(self,station):
		self.station = station

	def update(self):
		print ("Weather ON site is:" + str(self.station.GetWeather()))

def __main__():
	station = weatherStation()
	phone = PhoneWeatherService(station)
	webSite = WebsiteWeatherService(station)
	station.add(phone,webSite)

	station.Run()

__main__()

