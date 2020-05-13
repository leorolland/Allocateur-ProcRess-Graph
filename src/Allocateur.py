from src.Ressource import Ressource

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

  def __str__(self):
    """Affichage en string"""
    output = "       Ressources : \n"
    for r in self.ressources:
      output+= str(r) + " "
    output += "\n       Processus : \n"
    for p in self.processus:
      output+= str(p) + " "
    return output