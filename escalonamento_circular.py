# -*- coding : utf-8 -*-

from random import randint
from listacircular import ListaCircular
from processador import Processador
from processo import Processo

quantum = int(input("Digite o valor do quantum: "))
troca_contexto = int(input("Digite o valor da troca de contexto: "))
quant_process = int(input("Digite a quantidade de processos: "))

# quantum        = 2#randint(1,5)
# troca_contexto = 2#randint(1,3)
# quant_process  = 4#randint(1,5)

# valores = [3,7,4,5]

processos = ListaCircular()

for i in range(quant_process):
	tempo_processo = int(input("Tempo do processo {}: ".format(i+1)))
	processo = Processo(tempo_processo)
	processos.push(processo)

print ("Processo criados\n")
for i in range(len(processos)):
	print (processos[i])

proc = Processador(quantum,contexto=troca_contexto)
proc.execute(processos)

print ("\nOrdem terminados e seus valores\n")

for indice,valor in enumerate(proc.get_processos()):
	print ("{} - {}".format(indice+1,valor))
	print ("  - Turnarroud: {}u".format(valor.get_turnarroud()))
	print ("  - Espera: {}u\n".format(valor.get_tempo_espera()))

print("Dados do processador\n")
print("Valor da troca de contexto : {}u".format(proc.get_tempo_contexto()))
print("Valor do quantum: {}u".format(proc.get_quantum()))
print("Tempo total de turnaroud: {}u".format(proc.get_turnarround()))
print("Tempo medio de espera: {:.1f}u".format(proc.get_tempo_espera_medio()))


