class Thermometre():
	__c = 0
	__f = 0

	def __init__(self, c, f):
		
		self.__f = f
		self.__c = c


	def affich(self, temp):

		print(temp) 

	def get__c(self):
		return self.__c

	def set__c(self, c):
		
		if c <= -273:
			
			print("Non")
			c = 0
		
		else:

			self.__c = self.toCel(c)

	def get__f(self):
		return self.__f

	def set__f(self, f):
		
		if f <= -273:
			
			print("Non")
			f = 0
		
		else:

			self.__f = self.toFar(f)

	def toFar(self, c):
		return(c * 9/5) + 32

	def toCel(self, f):
		return(f - 32) * 5/9

leMercure = Thermometre(0 , 0)
leMercure.set__f(0)
leMercure.set__c(32)
print(leMercure.get__f())
print(leMercure.get__c())

