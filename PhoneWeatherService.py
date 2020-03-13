from IObserver import IObserver
class PhoneWeatherService(IObserver):
	"""docstring for PhoneWeatherService"""

	def __init__(self,IOBservable):
		super(PhoneWeatherService, self).__init__()
		self.OBservable = IOBservable
	
	def update(self):
		print("New Change in Observable parameter.")
		print(self.OBservable.GetObservableData())	 
		