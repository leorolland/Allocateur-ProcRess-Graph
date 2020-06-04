
from src.Allocateur import Allocateur
from src.Affichage import Affichage
from src.Shell import Shell
import time

def attenteInteractive(aff):
  aff.affichageGlobal()
  time.sleep(1)

def scenario0():
  print("Exécution du scénario 0")
  # Création allocateur
  alloc = Allocateur(countRessources=2)
  aff = Affichage(alloc)
  aff.affichageGlobal()
  # Création des processus
  attenteInteractive(aff)
  alloc.createProcessus("P1")

  attenteInteractive(aff)
  alloc.createProcessus("P2")

  attenteInteractive(aff)
  alloc.askForRessource("P1", "R0")

  attenteInteractive(aff)
  alloc.askForRessource("P2", "R1")

  attenteInteractive(aff)
  alloc.askForRessource("P2", "R0")

  attenteInteractive(aff)
  alloc.askForRessource("P1", "R1")
  # Boucle infinie shell
  Shell(alloc, aff)

def scenario1():
  print("Exécution du scénario 1")
  # Création allocateur
  alloc = Allocateur(countRessources=4)
  aff = Affichage(alloc)
  aff.affichageGlobal()
  # Création des processus du premier blocage
  attenteInteractive(aff)
  alloc.createProcessus("P1")

  attenteInteractive(aff)
  alloc.createProcessus("P2")

  attenteInteractive(aff)
  alloc.askForRessource("P1", "R0")

  attenteInteractive(aff)
  alloc.askForRessource("P2", "R1")

  attenteInteractive(aff)
  alloc.askForRessource("P2", "R0")

  attenteInteractive(aff)
  alloc.askForRessource("P1", "R1")
  # Création des processus du second blocage
  attenteInteractive(aff)
  alloc.createProcessus("A")

  attenteInteractive(aff)
  alloc.createProcessus("B")

  attenteInteractive(aff)
  alloc.askForRessource("A", "R2")

  attenteInteractive(aff)
  alloc.askForRessource("B", "R3")

  attenteInteractive(aff)
  alloc.askForRessource("B", "R2")

  attenteInteractive(aff)
  alloc.askForRessource("A", "R3")
  # Boucle infinie shell
  Shell(alloc, aff)

def scenario2():
  print("Exécution du scénario 2")
  # Création allocateur
  alloc = Allocateur(countRessources=4)
  aff = Affichage(alloc)
  aff.affichageGlobal()

  # Création des processus du premier blocage
  attenteInteractive(aff)
  alloc.createProcessus("P1")

  attenteInteractive(aff)
  alloc.createProcessus("P2")

  attenteInteractive(aff)
  alloc.askForRessource("P1", "R0")

  attenteInteractive(aff)
  alloc.askForRessource("P2", "R1")

  attenteInteractive(aff)
  alloc.askForRessource("P2", "R0")

  attenteInteractive(aff)
  alloc.askForRessource("P1", "R1")

  # Création des processus du second blocage lié au premier
  attenteInteractive(aff)
  alloc.createProcessus("A")

  attenteInteractive(aff)
  alloc.createProcessus("B")

  attenteInteractive(aff)
  alloc.askForRessource("A", "R2")

  attenteInteractive(aff)
  alloc.askForRessource("B", "R3")

  attenteInteractive(aff)
  alloc.askForRessource("B", "R2")

  attenteInteractive(aff)
  alloc.askForRessource("A", "R0")

  # Boucle infinie shell
  Shell(alloc, aff)

def scenario3():
  print("Exécution du scénario 3")
  # Création allocateur
  alloc = Allocateur(countRessources=3)
  aff = Affichage(alloc)
  aff.affichageGlobal()

  attenteInteractive(aff)
  alloc.createProcessus("P1")

  attenteInteractive(aff)
  alloc.createProcessus("P2")

  attenteInteractive(aff)
  alloc.askForRessource("P2", "R0")

  attenteInteractive(aff)
  alloc.askForRessource("P1", "R0")

  attenteInteractive(aff)
  alloc.createProcessus("A")

  attenteInteractive(aff)
  alloc.createProcessus("B")

  attenteInteractive(aff)
  alloc.askForRessource("A", "R1")

  attenteInteractive(aff)
  alloc.askForRessource("B", "R2")

  attenteInteractive(aff)
  alloc.askForRessource("P2", "R1")

  attenteInteractive(aff)
  alloc.askForRessource("P2", "R2")

  attenteInteractive(aff)
  alloc.askForRessource("A", "R0")

  attenteInteractive(aff)
  alloc.askForRessource("B", "R0")
  # Boucle infinie shell
  Shell(alloc, aff)

scenarios = [
  scenario0,
  scenario1,
  scenario2,
  scenario3
]