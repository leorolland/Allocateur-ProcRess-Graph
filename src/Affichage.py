import networkx as nx
import matplotlib.pyplot as plt
from collections import deque 

class Affichage(object):

	#Allocateur
	allocateur = None

	#Graphe
	G = nx.DiGraph()


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
			tmp = r.getAllocatedProcessus()
			dem = r.demandes
			if tmp != None:
				self.G.add_edge(r.getName(),tmp.getName())
			if dem != None:	
				for d in dem:
					self.G.add_edge(d.getName(),r.getName(),length=10)

			
	
	
	def affichageGlobal(self):
		# Mise a jour de l'affichage
		self.G.clear()
		self.addProcessus()
		self.addRessources()
		self.addLiens()

		colorNodes = []
		tailleNodes = []
		for n in self.G.nodes:
			if n[0] == 'R':
				colorNodes.append('red')
				tailleNodes.append(500)
			else:
				colorNodes.append('green')
				tailleNodes.append(1500)

		plt.clf() # Nettoyage du plot
		nx.draw(self.G, with_labels=True,node_color=colorNodes,node_size=tailleNodes) # Dessin du nouveau plot
		plt.pause(0.01) # Affichage non bloquant
		

	