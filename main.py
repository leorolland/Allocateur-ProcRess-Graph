from src.Allocateur import Allocateur
from src.Shell import Shell

if __name__ == "__main__":
  rc = int(input("Entrez le nombre de ressources : "))
  a = Allocateur(countRessources=rc)
  Shell(a)