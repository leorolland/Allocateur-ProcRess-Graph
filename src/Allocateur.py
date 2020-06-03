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
		# Suppression des demandes et allocations en ressources
		for r in self.ressources:
			self.libererRessource(name, r.getName())
		# Récupération de l'instance dans la liste des processus, None si absente
		inst = self.getProcessusInstance(name)
		# Suppression de cet élément dans la liste
		self.processus = [p for p in self.processus if p != inst]

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

	def attentesEntreProcessus(self):
		attentes = []
		for ress in self.ressources:
			allocatedProc = ress.getAllocatedProcessus()
			# Si la ressource est allouée
			if allocatedProc:
				# Pour chaque processus dans sa liste d'attente, on crée
				# une attente
				for attenteProc in ress.demandes:
					attentes.append((attenteProc, allocatedProc))
		return attentes

	def detecterBoucle(self, attentes, premier, courant=None):
		"""Fonction récursive renvoyant True si le processus "premier" est dans un interblocage"""
		# Si on a rebouclé sur le premier, on renvoie true
		if premier is courant:
			return True
		# Dans le cas du premier appel de la fonction, courant vaut None, il faut l'initialiser
		if not courant:
			courant = premier
		# Sinon on cherche l'élément suivant
		dependance = None
		for attente in attentes:
			if attente[0] is courant:
				dependance = attente[1]
		# Si il n'y a pas de suivant (dépendance) on renvoie false
		if not dependance:
			return False
		# Si il y en a une on continue le parcours
		return self.detecterBoucle(attentes, premier, dependance)

	def detecterInterbloquages(self):
		attentes = self.attentesEntreProcessus()
		processusBloques = []
		# Pour chaque processus, on suit le "chemin" de ses attentes
		# Si on reboucle sur le même processus, il y a interblocage
		# Si on tombe sur un processus qui n'attend aucun autre processus
		# il n'y a pas interblocage pour ce dernier
		for proc in self.processus:
			# On regarde si ce processus est dans une situation d'interblocage
			if self.detecterBoucle(attentes, premier=proc):
				processusBloques.append(proc)
		return processusBloques
				
	def resoudreInterblocage(self):
		procBloques = self.detecterInterbloquages()
		while len(procBloques):
			proc = procBloques[0]
			# On supprime proc de la liste d'attente d'une ressource demandée par proc
			for ress in self.ressources:
				if proc in ress.demandes:
					ress.retirerFileAttente(proc)
					break
			# On met a jour la liste des proc bloqués
			procBloques = self.detecterInterbloquages()

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