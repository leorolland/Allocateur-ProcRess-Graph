import networkx as nx
import matplotlib.pyplot as plt

class Affichage(object):

	#Allocateur
	allocateur = None

	#Graphe
	G = nx.Graph()

	def __init__(self, all):
		self.allocateur = all

	def addProcessus(self):
		for p in self.allocateur.processus:
			self.G.add_node(p.getName())

	def addRessources(self):
		for r in self.allocateur.ressources:
			self.G.add_node(r.getName())
	
	def affichageGlobal(self):
		# Mise a jour de l'affichage
		self.G.clear()
		self.addProcessus()
		plt.clf() # Nettoyage du plot
		nx.draw(self.G, with_labels=True) # Dessin du nouveau plot
		plt.pause(0.01) # Affichage non bloquant
		

	