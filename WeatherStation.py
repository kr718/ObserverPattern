from  IObservable import IObservable
from random import randint
import sys
import os
from time import sleep
class WeatherStation(IObservable):
	"""docstring for WeatherStation"""
	

	def __init__(self):
		super(WeatherStation, self).__init__()
		self.tmp = 0 
		self.humidity = 0

	def Run(self):
		#read sensors every 1 second.
		while(True):
			try:
				self.ReadSensors()
				sleep(1)
			except KeyboardInterrupt:
				print('Interrupted')
				try:
					sys.exit(0)
				except SystemExit:
					os._exit(0)

	def ReadSensors(self):
		currentTmp = randint(10,30)
		currenthumidity = randint(0,100)
		
		if currentTmp != self.tmp:
			self.tmp = currentTmp
			self.Notify()

		if currenthumidity != self.humidity:
			self.humidity = currenthumidity
			self.Notify()
		
	def GetObservableData(self):
		return [self.tmp,self.humidity]
