class Employe(): 

	def __init__(self, nom, salaire):
		super(Employe, self).__init__()
		
		self.nom = nom
		self.salaire = salaire

	def affich(self):

		print(self.nom, self.salaire) 


class Boucher(Employe): 

	def __init__(self, nom, salaire, listeViandes):
		super().__init__(nom, salaire)
		
		#self.nom = nom
		#self.salaire = salaire
		self.listeViandes = listeViandes

	def affich(self):
		super().affich()
		print(self.listeViandes) 

JeanMi = Employe("JeanMi", 30000)
JeanMi.affich()


Toto = Boucher("Toto", 45000, ["Agneau", "Veau", "Poulet"])
Toto.affich()
