# https://docs.python.org/fr/3/library/collections.html#collections.deque
from collections import deque 
from random import randint

class Ressource(object):
	
	# Nom de cette ressource
	name = ""

	# Queue d'attente type 'deque'
	demandes = None

	# Processus auquel cette ressource est allouée, None si non allouée
	processus = None

	def __init__(self, name=""):
		self.name = name
		self.demandes = deque()

	def ajouterFileAttente(self, processus):
		"""Ajoute un processus dans la file d'attente de cette ressource."""
		print("Ajout de " + str(processus) + " à la liste d'attente de " + str(self))
		# Ajout de l'élément à droite
		self.demandes.append(processus)
		# Mise à jour du composant
		self.update()

	def retirerFileAttente(self, processus):
		"""Supprime un processus de la file d'attente de cette ressource"""
		if (processus in self.demandes):
			self.demandes.remove(processus)
		# Mise à jour du composant
		self.update()

	def liberer(self):
		"""Détache le processus lié à cette ressource."""
		self.processus = None
		# Mise à jour du composant
		self.update()

	def getAllocatedProcessus(self):
		"""Renvoie le processus auquel cette ressource est alloué, None sinon"""
		return self.processus

	def update(self):
		"""Met à jour ce composant"""
		# Si aucun processus n'est alloué et qu'il y en a un en file d'attente
		print("Mise à jour de la ressource " + self.name)
		if not self.processus and len(self.demandes)>0:
			# On l'alloue a cette ressource
			self.processus = self.demandes.popleft()
			print("La ressource " + self.name + " à été attribuée au processus " + str(self.processus))

	def getName(self):
		"""Renvoie le nom de cette ressource"""
		return self.name		

	def __str__(self):
		"""Affichage en string"""
		return self.name + "(" + ("occupée" if self.processus else "libre") + ")"

		
