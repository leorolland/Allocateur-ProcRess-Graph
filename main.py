from src.Allocateur import Allocateur
from src.Shell import Shell
from src.Affichage import Affichage

if __name__ == "__main__":
  rc = int(input("Entrez le nombre de ressources : "))
  a = Allocateur(countRessources=rc)
  aff = Affichage(a)
  Shell(a, aff)