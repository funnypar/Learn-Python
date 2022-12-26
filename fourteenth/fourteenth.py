class CountryLibrary:
	counter = 0
	def __init__(self, name, pages, writer):
		CountryLibrary.counter += 1
		self.name = name
		self.pages = pages
		self.writer = writer
	def getBookName(self):
		print("The 📙 name is \"%s\" " % self.name)
	def getBookPages(self):
		print("The 📙 has \"%s\" pages  " % self.pages)
	def getBookWriter(self):
		print("This 📙 written by \"%s\"  " % self.writer)
	def __info__(self):
		# print("The 📙 name is \"%s\" " % self.name)
		# print("The 📙 has \"%s\" pages  " % self.pages)
		# print("This 📙 written by \"%s\"  " % self.writer)
		CountryLibrary.getBookName(self)
		CountryLibrary.getBookPages(self)
		CountryLibrary.getBookWriter(self)

class CityLibrary(CountryLibrary):
	pass

educated = CountryLibrary("educated", 126, "Tara")
# educated.getBookName()
# educated.getBookPages()
# educated.getBookWriter()
educated.__info__()

saye = CityLibrary("Saye", 90, "Hoshang Ebtehaj")
saye.__info__()
