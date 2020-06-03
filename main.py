from src.Allocateur import Allocateur
from src.Shell import Shell
from src.Affichage import Affichage

from src.Scenarios import scenarios

if __name__ == "__main__":
  mode = input("Choisissez un mode (scenario/libre) :")
  if mode == "libre":
    print("Mode libre.")
    rc = int(input("Entrez le nombre de ressources : "))
    a = Allocateur(countRessources=rc)
    aff = Affichage(a)
    Shell(a, aff)
  else:
    print("Mode scénario.")
    print("Scénario 0 : interblocage simple")
    print("Scénario 1 : interblocage simple x2")
    n = int(input("Entrez un numéro de scénario : "))
    func = scenarios[n]
    func()