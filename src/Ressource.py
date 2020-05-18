# https://docs.python.org/fr/3/library/collections.html#collections.deque
from collections import deque 
from random import randint

class Ressource(object):
	
	# Nom de cette ressource
	name = ""

	# Queue d'attente type 'deque'
	demandes = deque()

	# Processus auquel cette ressource est allouée, None si non allouée
	processus = None

	def __init__(self, name=""):
		self.name = name

	def ajouterFileAttente(self, processus):
		"""Ajoute un processus dans la file d'attente de cette ressource."""
		# Ajout de l'élément à droite
		self.demandes.append(processus)
		# Affichage de la queue
		print(self.demandes)
		# Mise à jour du composant
		self.update()

	def retirerFileAttente(self, processus):
		"""Supprime un processus de la file d'attente de cette ressource"""
		self.demandes = [d for d in self.demandes if d != processus]
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
		if not self.processus and len(self.demandes)>0:
			# On l'alloue a cette ressource
			self.processus = self.demandes.popleft()
			print("La ressource " + str(self.name) + " à été attribuée au processus " + str(self.processus))

	def __str__(self):
		"""Affichage en string"""
		return self.name + "(" + ("occupée" if self.processus else "libre") + ")"

		
