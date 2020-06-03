## Règles du modèle
L’allocateur aura un nombre limité de ressource fixé au lancement du programme.
Respectera les règles R1 à R11 
Pourra exécuter les ordres de O1 à O8 exécutés par `ReadUserInstructions`

## Règles
- R1 chaque ressource est attribuée à au plus un processus ;
- R2 si le processus demandeur n’est pas connu de l’allocateur, il est créé ;
- R3 une ressource demandée disponible est immédiatement attribuée au
processus demandeur ;
- R4 si la ressource est déjà attribuée, le processus demandeur est mis en
attente de la ressource ;
- R5 si une ressource est libérée, elle est attribuée au plus ancien processus
demandeur, ou bien elle devient disponible si elle n’est plus demandée ;
- R6 un processus est actif si toutes ses demandes de ressources ont été
satisfaites ;

- R7 un processus est bloqué s’il est en attente d’au moins une des res-
sources demandées ;

- R8 un processus actif peut demander plusieurs ressources à la fois, il devient bloqué si au moins l’une des ressources demandées est indisponible, mais ce blocage n’interviendra qu’à la fin du traitement de la demande ;

- R9 un processus actif peut libérer une ou plusieurs ressources qu’il dé-
tient ;

- R10 un processus bloqué ne peut demander ni libérer une ressource tant
qu’il n’est pas redevenu actif ;
- R11 un processus détruit libére toutes les ressources qu’il détient.
- R12 : En cas d’interblocage (l’interblocage est défini plus bas), les ordres acceptés sont limités à O5, O6, O7, O8 et O9 (affichage et déblocage).
- R13 : A chaque changement de l’état interne, le modèle vérifie si il y a interblocage.

## Règles de modélisation invariantes
- MI1 : Les sommets du graphe représentent les processus et les ressources
- MI2 : Les arcs du graphe représentent 
Si arc de ressource vers un processus : une allocation
Si arc d’un processus vers ressource : une demande
- MI3 : Un interblocage intervient dans le cas où deux processus demandent respectivement une ressource allouée à l’autre.
- MI4 : Affichage des ordres :
- O5 : Affichage de la queue de processus en attente en “file indienne” sur un graphe dirigé, queue pour chaque ressource.
- O6 : Affichage d’un sous graphe avec uniquement les processus actifs
- O7 : Affichage des attentes par fermeture transitive du graphe, en gardant seulement les arcs significatifs.
- O8 : Affichage des processus interbloqués et des ressources liées
- O9 : Résolution de l'interblocage

## Règles de modélisation variantes
- MV1 : Crée un sommet “processus” sur le graphe
- MV2 : Supprime le sommet du graphe et supprime les arcs partant de ce - noeud (demandes) et les arcs entrants (allocations à ce processus).
- MV3 : Ajoute le processus à la file d’attente du noeud, ajoute un arc - du processus vers la ressource.
- MV4 : Supprime l’arc d’allocation de la ressource vers le processus

## Création éventuelle d’ordres (déblocage inter-processus)
Ajout de l’ordre O9 destiné résoudre l’interblocage

## Détection et correction de l’interblocage
- Détection d’une boucle dans le graphe des interdépendances entre processus. Le graphes d’interdépendances entre processus résulte de la fermeture transitive utilisée pour O7, et ne présente pas les ressources.
- Il faut rompre la boucle, on prend un processus bloqué au hasard, on le retire de la liste d'attente de sa ressource demandée, on continue tant que l'interblocage persiste.

## Test de l’interblocage simple avec 2 processus

- ordre = création de P1 et P2 (O1)
- File R1 = (P1)
- File R2 = (P2)
- A ce stade l’allocateur va allouer R1 à P1 et R2 à P2.
- File R1 = (P2)
- File R2 = (P1)
- L’allocateur doit détecter un interblocage et le résoudre si demande
- règles = R12, R13
