from collections import deque 

class Processus(object):

	#nom du processus
	name = ""

	#liste des ressources allouées
	ressources = deque()

	def __init__(self,name=""):
		self.name = name

	def update(self):
		pass

	def getName(self):
		return self.name

	def __str__(self):
		return self.name
		