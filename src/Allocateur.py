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
		# Récupération de l'instance dans la liste des processus, None si absente
		inst = next((p for p in self.processus if p.getName() == name), None)
		if not inst:
			print("Aucun processus trouvé pour le nom : " + name)
			return
		# Suppression de cet élément dans la liste
		self.processus = [p for p in self.processus if p != inst]
		# Suppression des demandes et allocations en ressources
		for r in self.ressources:
			# Si une ressource etait allouée à ce processus
			if r.getAllocatedProcessus() == inst:
				# On libère la ressource
				r.liberer()
			# Dans tous les cas, on le retire de la file d'attente
			r.retirerFileAttente(inst)

	def askForRessource(self, processusName, ressourceName):
		"""Demande l'attribution d'une ressource à un processus"""
		proc = self.getProcessusInstance(processusName)
		ress = self.getRessourceInstance(ressourceName)
		if proc and ress:
			# TODO : Vérifier l'interblocage
			# Ajout du processus à la liste d'attente
			ress.ajouterFileAttente(proc)
	
	def libererRessource(self, processusName, ressourceName):
		"""Libération d'une ressource par un processus"""
		proc = self.getProcessusInstance(processusName)
		ress = self.getRessourceInstance(ressourceName)
		if proc and ress:
			# On retire le processus de la file d'attente
			ress.retirerFileAttente(proc)
			# Si la ressource était allouée à ce processus, on la libère
			if ress.getAllocatedProcessus() == proc:
				ress.liberer()

	def getProcessusInstance(self, processusName):
		"""Renvoie l'instance d'un processus"""
		proc = next((p for p in self.processus if p.getName() == processusName), None)
		if not proc:
			print("Le processus " + processusName + " n'éxiste pas")
		return proc

	def getRessourceInstance(self, ressourceName):
		"""Renvoie l'instance d'une ressource""" 
		ress = next((r for r in self.ressources if r.getName() == ressourceName), None)
		if not ress:
			print("La ressource " + ressourceName + " n'éxiste pas")
		return ress

	def __str__(self):
		"""Affichage en string"""
		output = "       Ressources : \n"
		for r in self.ressources:
			output+= str(r) + " "
		output += "\n       Processus : \n"
		for p in self.processus:
			output+= str(p) + " "
		return output