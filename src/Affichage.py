import networkx as nx
import matplotlib.pyplot as plt
from collections import deque 

class Affichage(object):

	#Allocateur
	allocateur = None

	#Graphe
	G = nx.Graph()

	#liste des liens
	liens = deque()

	def __init__(self, all):
		self.allocateur = all

	def addProcessus(self):
		for p in self.allocateur.processus:
			self.G.add_node(p.getName())

	def addRessources(self):
		for r in self.allocateur.ressources:
			self.G.add_node(r.getName())

	def addLiens(self):
		for r in self.allocateur.ressources:
			if r.getAllocatedProcessus():
				self.liens.append((r,r.getAllocatedProcessus()))
				#self.G.add_edge((r.getName(),r.getAllocatedProcessus().getName()))
	
	
	def affichageGlobal(self):
		# Mise a jour de l'affichage
		self.G.clear()
		self.addProcessus()
		self.addRessources()
		self.addLiens()
		for l in self.liens:
			self.G.add_edge(*l)
		plt.clf() # Nettoyage du plot
		nx.draw(self.G, with_labels=True) # Dessin du nouveau plot
		plt.pause(0.01) # Affichage non bloquant
		

	