# encoding: utf-8

'''
	Implementação da rede Perceptron
	Autor: Marcos Castro
'''

import random, copy

class Perceptron:

	def __init__(self, amostras, saidas, taxa_aprendizado=0.01, epocas=1000, limiar=-1):

		self.amostras = amostras # todas as amostras
		self.saidas = saidas # saídas respectivas de cada amostra
		self.taxa_aprendizado = taxa_aprendizado # taxa de aprendizado (entre 0 e 1)
		self.epocas = epocas # número de épocas
		self.limiar = limiar # limiar
		self.num_amostras = len(amostras) # quantidade de amostras
		self.num_amostra = len(amostras[0]) # quantidade de elementos por cada amostra
		self.pesos = [] # vetor dos pesos


	# função utilizada para treinar a rede
	def treinar(self):

		# adiciona -1 para cada amostra
		for amostra in self.amostras:
			amostra.insert(0, -1)

		# inicia o vetor de pesos com valores aleatórios pequenos
		for i in range(self.num_amostra):
			self.pesos.append(random.random())
			print('Pesos Iniciais %s' % self.pesos[i])

		# insere o limiar no vetor de pesos
		self.pesos.insert(0, self.limiar)

		num_epocas = 0 # inicia o contador de épocas
		
		while True:

			erro = False # erro inicialmente inexiste

			# para todas as amostras de treinamento
			for i in range(self.num_amostras):
				
				u = 0
				'''
					realiza o somatório, o limite (self.num_amostra + 1) 
					é porque foi inserido o -1 em cada amostra
				'''
				for j in range(self.num_amostra + 1):
					u += self.pesos[j] * self.amostras[i][j]
				

				# obtém a saída da rede utilizando a função de ativação
				y = self.sinal(u)

				# verifica se a saída da rede é diferente da saída desejada
				if y != self.saidas[i]:

					# calcula o erro: subtração entre a saída desejada e a saída da rede
					erro_aux = self.saidas[i] - y

					# faz o ajuste dos pesos para cada elemento da amostra
					for j in range (self.num_amostra + 1):
						self.pesos[j] = self.pesos[j] + self.taxa_aprendizado * erro_aux * self.amostras[i][j]
						print(self.pesos[j])
					erro = True # se entrou, é porque o erro ainda existe
			
			num_epocas += 1 # incrementa o número de épocas

			print(num_epocas)


			# critério de parada é pelo número de épocas ou se não existir erro
			if num_epocas == 5:
			#if num_epocas > self.epocas or not erro:
				break


	# função utilizada para testar a rede
	# recebe uma amostra a ser classificada e os nomes das classes
	# utiliza função sinal, se é -1 então é classe1, senão é classe2
	def testar(self, amostra, classe1, classe2):

		# insere o -1
		amostra.insert(0, -1)

		'''
			utiliza-se o vetor de pesos ajustado
			durante o treinamento da rede
		'''
		u = 0
		for i in range(self.num_amostra + 1):
			u += self.pesos[i] * amostra[i]

		# calcula a saída da rede
		y = self.sinal(u)

		# verifica a qual classe pertence
		if y == -1:
			print('A amostra %s pertence a classe %s' % (amostra, classe1) )
		else:
			print('A amostra %s pertence a classe %s' % (amostra, classe2) )


	def degrau(self, u):
		return 1 if u >= 0 else 0


	def sinal(self, u): # é a mesma função degrau bipolar
		return 1 if u >= 0 else -1


if __name__ == "__main__":

	# todas as amostras (total de 4 amostras)
	amostras = [[-0.651,    0.1097,    4.0009],
				[-1.449,    0.8896,    4.4005],
				[2.0851,    0.6876,    12.071],
				[0.2626,    1.1476,    7.7985],
				[0.6418,    1.0234,    7.0427],
				[0.2569,    0.6731,    8.3265],
				[1.1155,    0.6043,    7.4446],
				[0.0914,    0.3399,    7.0677],
				[0.0121,    0.5256,    4.6316],
				[-0.042,    0.4661,    5.4323],
				[0.4341,    0.6871,    8.2287],
				[0.2735,    1.0287,    7.1934],
				[0.4839,    0.4851,    7.4851],
				[0.4089,    -0.126,    5.5019],
				[1.4391,    0.1614,    8.5843],
				[-0.911,    -0.197,    2.1962],
				[0.3654,    1.0475,    7.4858],
				[0.2144,    0.7515,    7.1699],
				[0.2013,    1.0014,    6.5489],
				[0.6483,    0.2183,    5.8991],
				[-0.114,   	0.2242,    7.2435],
				[-0.797,   	0.8795,    3.8762],
				[-1.062,   	0.6366,    2.4707],
				[0.5307,    0.1285,    5.6883],
				[-1.221,   	0.7777,    1.7252],
				[0.3957,    0.1076,    5.6623],
				[-0.101,   	0.5989,    7.1812],
				[2.4482,    0.9455,    11.209],
				[2.0149,    0.6192,    10.926],
				[0.2012,    0.2611,    5.4631]]


	# saídas desejadas de cada amostra
	saidas = [-1, -1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, -1, 1, -1, 1]

	# conjunto de amostras de testes
	testes = copy.deepcopy(amostras)

	# cria uma rede Perceptron
	rede = Perceptron(amostras=amostras, saidas=saidas, 
						taxa_aprendizado=0.01, epocas=1000)

	# treina a rede
	rede.treinar()

	for teste in testes:
		rede.testar(teste, 'P1', 'P2')