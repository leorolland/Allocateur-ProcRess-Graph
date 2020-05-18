from collections import deque 

class Processus(object):

    #nom du processus
    name = ""

    #liste des ressources allouées
    ressources = deque()

    def __init__(self,name=""):
        self.name = name

    def ajouterRessources(self,ressource):
        "Ajoute une ressouce dans la liste des ressouces allouées de ce processus"
        self.ressources.append(ressource)
        #affichage de la liste
        print(self.ressources)
        