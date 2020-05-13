import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()


while (True):
	nom = input("Ajouter un noeud (entrez un nombre): ")
	# Ajout du noeud
	G.add_node(nom)


	# Mise a jour de l'affichage
	plt.clf() # Nettoyage du plot
	nx.draw(G, with_labels=True) # Dessin du nouveau plot
	plt.pause(0.01) # Affichage non bloquant

