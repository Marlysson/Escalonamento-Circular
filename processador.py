# -*- coding : utf-8 -*-

class Processador(object):
	def __init__(self,quantum,contexto=0):

		self.linha_do_tempo = 0
		self.quantum = quantum
		self.processos_terminados = []
		self.troca_contexto = contexto
		
	def get_quantum(self):
		return self.quantum

	def get_processos(self):
		return self.processos_terminados

	def get_tempo_espera_medio(self):
		tempo = 0

		for processo in self.processos_terminados:
			tempo += processo.get_tempo_espera()

		return tempo / len(self.processos_terminados)

	def get_turnarround(self):
		return self.linha_do_tempo

	def get_turnaround_medio(self):
		return self.get_turnarround() / len(self.processos_terminados)

	def get_tempo_contexto(self):
		return self.troca_contexto

	def execute(self,processos):

		processo_atual = processos[0]

		while len(processos) > 0:	
			#pega um processo para executar
			processo = processo_atual

			#executa o processo e armazena o valor executado
			passo = processo.executar(self.quantum)

			#incrementa na linha do tempo do processador o tempo executado
			self.linha_do_tempo += passo

			#algumas definicoes caso o processo termine de ser executado
			if processo.get_contexto("restante") == 0:

				processo.set_turnarroud(self.linha_do_tempo)
				processo.set_tempo_espera(self.linha_do_tempo - processo.get_tempo_cpu())

				self.processos_terminados.append(processo)
				
				processos.remove(processo)

				#nao incrementar contexto apos o ultimo processo acabar
				if len(processos) > 0:
					self.linha_do_tempo += self.troca_contexto

			#senao incrementa a troca de contexto apos a execucao
			else:

				#aumenta contexto depois da execucao do processo
				self.linha_do_tempo += self.troca_contexto

			processo_atual = processo.prox

