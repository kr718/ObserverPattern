class IObservable(object):
	"""docstring for IObservable"""
	

	def __init__(self):
		self.ListOfObservers = []
	
	def Add(self, *observers):
		for observer in observers:
			self.ListOfObservers.append(observer)

	def Remove(self, observer):
		if observer in self.ListOfObservers:
			self.ListOfObservers.remove(observer)

	def Notify(self):
		for observer in self.ListOfObservers:
			observer.update()

	def GetObservableDate(self):
		pass
