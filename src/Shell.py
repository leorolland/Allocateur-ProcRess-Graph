class Shell(object):
	"""Interface de dialogue avec l'utilisateur"""

	# Allocateur
	a = None

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

	# Liste des commandes
	cmds = {
		1: createProcessus, # 01 - Créer processus
		2: removeProcessus, # 02 - Détruire processus
		3: askForRessource,
		4: libererRessource
	}

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
		print(" 1 - Créer un processus")
		print(" 2 - Détruire un processus")
		print(" 3 - Demander une ressource pour un processus")
		print(" 4 - Libérer une ressource d'un processus")
		n = int(input("Entrez le numéro de commande : "))
		# Récupération et appel de la fonction associée au numéro
		func = self.cmds.get(n)
		func(self)

