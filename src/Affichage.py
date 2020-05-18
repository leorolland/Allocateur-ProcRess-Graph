import networkx as nx
import matplotlib.pyplot as plt

class Affichage(object):

    #Allocateur
    allocateur = None

    #Graphe
    G = nx.Graph()

    def __init__(self, all:Allocateur):
        self.allocateur = all

    def addProcessus(self):
        for p in self.allocateur.processus:
            G.add_node(p.getName())
    
    def affichageGlobal(self):
        # Mise a jour de l'affichage
	    plt.clf() # Nettoyage du plot
	    nx.draw(G, with_labels=True) # Dessin du nouveau plot
	    plt.pause(0.01) # Affichage non bloquant
        

    