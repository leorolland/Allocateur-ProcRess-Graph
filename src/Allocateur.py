from src.Ressource import Ressource
from src.Processus import Processus

class Allocateur(object):
	
	# Liste des ressources
	ressources = []

	# Liste des processus
	processus = []

	def __init__(self, countRessources: int):
		"""Création d'un allocateur avec un nombre défini de ressources"""
		for i in range(countRessources):
			self.ressources.append(Ressource("R" + str(i)))

	def update(self):
		"""Met à jour l'allocateur et ses composants"""
		for c in self.ressources + self.processus:
			c.update()

	def createProcessus(self, name):
		"""Crée un processus"""
		self.processus.append(Processus(name))

	def removeProcessus(self, name):
		"""Supprime un processus"""
		# Récupération de l'instance 
		
		# Suppression d'un processus de la liste
		self.processus = [p for p in self.processus if p.getName() != name]
		# Suppression des demandes et allocations en ressources
		for r in self.ressources:
			# Si une ressource etait allouée à ce processus
			if r.getAllocatedProcessus().getName() == name:
				# On libère la ressource
				r.liberer()
			# Dans tous les cas, on le retire de la file d'attente
			r.retirer(name)


	def __str__(self):
		"""Affichage en string"""
		output = "       Ressources : \n"
		for r in self.ressources:
			output+= str(r) + " "
		output += "\n       Processus : \n"
		for p in self.processus:
			output+= str(p) + " "
		return output