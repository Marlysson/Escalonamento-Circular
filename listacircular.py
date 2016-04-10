
class ListaCircular(object):

	def __init__(self):
		self.inicio = None
		self.final  = None

	def __getitem__(self,index):
		cont = 0
		atual = self.inicio

		while True:
			if cont == index:
				return atual
			else:
				atual = atual.prox

			cont += 1

	def __len__(self):
		cont = 0
		atual = self.inicio
		inicio = None

		while atual != inicio:
			cont += 1
			atual = atual.prox
			inicio = self.inicio

		return cont

	def __iter__(self):
		return self

	def __next__(self):
		anterior = None

		'''
			self.final.prox = None
			if self.inicio == None:
			
			Iterador FOR
			- Cortando uma lista circular, apontando o fim
			para None e nao para o inicio.
		'''


		if self.inicio.prox == self.inicio:
			raise StopIteration()
		else:
			anterior = self.inicio
			self.inicio = self.inicio.prox

			return anterior


	def __repr__(self):
		
		representacao = "["
		atual = self.inicio
		#caso em que tenha elementos na lista
		if atual != None:

			while True:

				if atual != self.final:
					representacao += "{}, ".format(atual)
				else:
					representacao += "{}".format(atual)

				atual = atual.prox

				if atual == self.final.prox:
					break

		representacao += "]"
		
		return representacao


	def push(self,novo):

		if self.inicio == None:
			
			self.inicio = novo
			self.final  = novo
			self.final.prox = self.inicio

		else:

			novo.prox = self.inicio
			self.final.prox = novo
			self.final = novo

	def remove(self,elemento=None):
		
		#Caso em que a lista nao esteja vazia
		if self.inicio != None:
			
			#Caso em que a lista tenha 1 elemento
			if self.inicio == self.inicio.prox:

				self.inicio = None
				self.final  = None

			#Lista tem mais de 1 elemento
			else:

				atual = self.inicio
				anterior = None

				#Verifica se nao foi passado nenhum parametro no metodo
				#Entao elimina o ultimo elemento
				if elemento == None:

					while atual != self.final:
						anterior = atual
						atual = atual.prox

					anterior.prox = self.inicio
					self.final = anterior
					self.final.prox = self.inicio

				#deseja-se remover um elemento especifico
				else:

					while True:
						if elemento == atual:
							break
						else:
							anterior = atual
							atual = atual.prox

					#removendo do inicio
					if atual == self.inicio:
						self.inicio = atual.prox
						self.final.prox = self.inicio

					#removendo do final
					elif atual == self.final:
						self.final = anterior
						self.final.prox = self.inicio
						# anterior.prox = self.inicio
					
					#removendo do meio
					else:
						anterior.prox = atual.prox

					del(atual)						

	
