
class Processo(object):
	
	cont = 0

	def __init__(self,tempo):
		self.__class__.cont += 1
		self.pid = self.cont
		self.tempo_cpu = tempo
		self.contexto = {"tempo_restante": tempo, 
						 "tempo_espera": 0}
		self.turnarroud = 0
		self.prox = None
		
	def set_tempo_espera(self,tempo):
		self.contexto["tempo_espera"] = tempo

	def get_tempo_espera(self):
		return self.contexto.get("tempo_espera")

	def get_pid(self):
		return self.pid
		
	def get_contexto(self,valor):

		if valor == "espera":
			return self.contexto.get("tempo_espera")
		elif valor == "restante":
			return self.contexto.get("tempo_restante")

	def get_tempo_cpu(self):
		return self.tempo_cpu

	def executar(self,quantum):
		'''
			Se o tempo restante for maior ou igual ao quantum:
				- aumenta o passo do quantum
			Se for menor ao quantum:
				- aumenta o valor restante para completar o valor do processo

			Returna o passo que foi executado para usar na linha do tempo
			do processador.
			
		'''

		if self.contexto["tempo_restante"] >= quantum:
			passo = quantum

			self.contexto["tempo_restante"] -= passo

		elif self.contexto["tempo_restante"] < quantum:

			passo = self.contexto["tempo_restante"]
			self.contexto["tempo_restante"] = 0
		
		return passo


	def get_turnarroud(self):
		return self.turnarroud

	def set_turnarroud(self,tempo):
		self.turnarroud = tempo

	def __repr__(self):
		return "Processo(pid={}, tempo={})".format(self.pid,self.tempo_cpu)
