import sys

class Shell(object):
	"""Interface de dialogue avec l'utilisateur"""

	# Allocateur
	a = None

	def quit(self):
		sys.exit()

	def createProcessus(self):
		"""O1 - Créer un processus"""
		name = input("Entrez le nom du processus : ")
		self.a.createProcessus(name)

	def removeProcessus(self):
		"""O2 - Détruire un processus"""
		name = input("Entrez le nom du processus à détruire: ")
		self.a.removeProcessus(name)
	
	def askForRessource(self):
		"""O3 - Demande de ressource par un processus"""
		procName = input("Entrez le nom du processus : ")
		ressName = input("Entrez le nom de la ressource : ")
		self.a.askForRessource(procName, ressName)

	def libererRessource(self):
		"""O4 - Libération d’une ressource par un processus"""
		ressName = input("Entrez le nom de la ressource : ")
		procName = input("Entrez le nom du processus : ")
		self.a.libererRessource(procName, ressName)

	def afficherFilesAttente(self):
		"""O5 - Affichage des files d’attente par ressource"""
		ress = self.a.ressources
		print("Affichage des files d'attentes :")
		for r in ress:
			print("   " + str(r))
			liste = ""
			for demande in r.demandes:
				liste += str(demande) + " "
			print("      " + liste)

	def afficherProcessusActifs(self):
		"""06 - Affichage des processus actifs"""
		print("Affichage des processus actifs :")
		for r in self.a.ressources:
			allocatedProc = a.getAllocatedProcessus(self)
			if (allocatedProc):
				print(str(allocatedProc))
			
	# Liste des commandes
	cmds = [
		quit,
		createProcessus, # 01 - Créer processus
		removeProcessus, # 02 - Détruire processus
		askForRessource, # 03
		libererRessource, # 04
		afficherFilesAttente, # 05
		afficherProcessusActifs, # 06
	]

	def __init__(self, allocateur, aff):
		self.a = allocateur
		# Boucle principale du programme
		while (True):
			aff.affichageGlobal()
			print(str(self.a))
			self.mainMenu()
			self.a.update()

	def mainMenu(self):
		"""Affichage et input du menu principal"""
		print("---- Menu principal ----")
		print("Liste des ordres :")
		print(" 0 - Quitter")
		print(" 1 - Créer un processus")
		print(" 2 - Détruire un processus")
		print(" 3 - Demander une ressource pour un processus")
		print(" 4 - Libérer une ressource d'un processus")
		print(" 5 - Affichage des listes d'attente par processus")
		n = int(input("Entrez le numéro de commande : "))
		func = self.cmds[n]
		func(self)

