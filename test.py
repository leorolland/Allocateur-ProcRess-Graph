import networkx as nx
import matplotlib.pyplot as plt

if __name__ == "__main__":
	G = nx.Graph()
	tableNoeuds = []
	ind = 0

	"""
	while (True):
		nom = input("Ajouter un noeud (entrez un nombre): ")
		# Ajout du noeud
		G.add_node(nom)
		tableNoeuds.insert(ind,nom)
		ind = ind + 1

	
		if len(G.nodes) > 1:
			arc = input("Connecter les deux derniers arcs ? (o/n) ")
			if arc == 'o':
				G.add_edge(tableNoeuds[len(tableNoeuds)-1], tableNoeuds[len(tableNoeuds)-2])
	
	"""
	G.add_node(1)
	G.add_node(2)
	G.add_edge(1,2)

	# Mise a jour de l'affichage
	plt.clf() # Nettoyage du plot
	nx.draw(G, with_labels=True) # Dessin du nouveau plot
	plt.pause(0.01) # Affichage non bloquant
    #plt.show()

