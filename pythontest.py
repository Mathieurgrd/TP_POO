#class test
import random

class Bateau():
	"""docstring for MyClass"""

	def __init__(self, nom, taille):
		super(Bateau, self).__init__()
		
		self.nom = nom
		self.taille = taille
		print("Constructeur appelé !")

	def presentationBateau(self):
		print("Je suis un bateau et mon nom est " + self.nom + "! Bonjour ! ")

	def increaseSize(self, arg):

		if arg < 0 : 
			print("Non")
		else :
			self.taille = self.taille +  arg 
			print(self.taille)

	def __del__(self):
		print("Le bateau", self.nom, " à coulé, Bloup !")

	def __lt__(self, bateau):

		return self.taille < bateau.taille
		

bateauSympa = Bateau("Le Beau Bateau", 5)
bateauCool  = Bateau("Le Cool Boat", 6)

print(bateauCool < bateauSympa) 

for x in range(50):
	    for x in range(x):
			print("Hello World")
		print(x)



#liste = [bateauCool, bateauSympa]

#for x in liste: 
#	x.presentationBateau()


#x = " \n Goodbye World \n"

#for x in x:
#	print(x)
#	for x in x:
#		print(x)




#bateauSympa.increaseSize(-6)

#print(bateauSympa.nom)
#print("La taille du bateau est ", bateauCool.taille)

#bateauCool.presentationBateau()
#bateauSympa.presentationBateau()

#mytuple = (bateauSympa.nom, bateauCool.nom)

#for x in mytuple:
  #print(x)