class Marque():

	def __init__(self, nom, listeVoiture):
		super(Marque, self).__init__()
		
		self.nom = nom
		self.listeVoiture = listeVoiture



class Voiture():


	def __init__(self, nom, Marque):
		super(Voiture, self).__init__()
		
		self.nom = nom
		self.Marque = Marque


dacia = Marque("Dacia" , [""])

duster = Voiture("Duster" , dacia)
sandero = Voiture("Sandero", dacia )

dacia.listeVoiture.append([sandero, duster]) 

print(sandero.Marque.nom)

dacia2 = Marque("Dacia" , [""])

dacia3 = dacia
print(dacia3 == dacia) 
#print(dacia.nom == dacia2.nom)