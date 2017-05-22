#!/usr/bin/env python
# -*- coding: utf-8 -*-

# aplicativo para verificar se o ser vivo eh quadrupede ou bipede
# valvula A = 1, valvula B = -1
# cao = [-1,-1,1,1] | resposta = 1
# gato = [1,1,1,1] | resposta = 1
# cavalo = [1,1,-1,1] | resposta = 1
# homem = [-1,-1,-1,1] | resposta = -1

import random, copy

# entradas
x =     [[0.4329,   -1.3719,    0.7022,   -0.8535],
        [0.3024,    0.2286,    0.8630,    2.7909],
        [0.1349,   -0.6445,    1.0530,    0.5687],
        [0.3374,   -1.7163,    0.3670,   -0.6283],
        [1.1434,   -0.0485,    0.6637,    1.2606],
        [1.3749,   -0.5071,    0.4464,    1.3009],
        [0.7221,   -0.7587,    0.7681,   -0.5592],
        [0.4403,   -0.8072,    0.5154,   -0.3129],
        [-0.5231,   0.3548,    0.2538,    1.5776],
        [0.3255,   -2.0000,    0.7112,   -1.1209],
        [0.5824,    1.3915,   -0.2291,    4.1735],
        [0.1340,    0.6081,    0.4450,    3.2230],
        [0.1480,   -0.2988,    0.4778,    0.8649],
        [0.7359,    0.1869,   -0.0872,    2.3584],
        [0.7115,   -1.1469,    0.3394,    0.9573],
        [0.8251,   -1.2840,    0.8452,    1.2382],
        [0.1569,    0.3712,    0.8825,    1.7633],
        [0.0033,    0.6835,    0.5389,    2.8249],
        [0.4243,    0.8313,    0.2634,    3.5855],
        [1.0490,    0.1326,    0.9138,    1.9792],
        [1.4276,    0.5331,   -0.0145,    3.7286],
        [0.5971,    1.4865,    0.2904,    4.6069],
        [0.8475,    2.1479,    0.3179,    5.8235],
        [1.3967,   -0.4171,    0.6443,    1.3927],
        [0.0044,    1.5378,    0.6099,    4.7755],
        [0.2201,   -0.5668,    0.0515,    0.7829],
        [0.6300,   -1.2480,    0.8591,    0.8093],
        [-0.2479,   0.8960,    0.0547,    1.7381],
        [-0.3088,  -0.0929,    0.8659,    1.5483],
        [-0.5180,   1.4974,    0.5453,    2.3993],
        [0.6833,    0.8266,    0.0829,    2.8864],
        [0.4353,   -1.4066,    0.4207,   -0.4879],
        [-0.1069,  -3.2329,    0.1856,   -2.4572],
        [0.4662,    0.6261,    0.7304,    3.4370],
        [0.8298,   -1.4089,    0.3119,    1.3235]]
# pesos (sinapses)
num_amostra = len(x[0])
w = []

for i in range(num_amostra):
    w.append(random.random())
    print('Pesos Iniciais %s' % w[i])

# respostas esperadas
t = [1,-1,-1,-1,1,1,1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,-1,1,1,1,-1,-1,-1]
# bias (ajuste fino)
b = 0
#saida
y = 0
# numero maximo de interacoes
max_int = 10
# taxa de aprendizado
taxa_aprendizado = 0.0025
#soma
soma = 0

# nome da valvula
valvula = ""
# resposta = acerto ou falha
resposta = ""

# dicionario de dados
d = {'-1' : 'A', 
     '1' : 'B' }

print("Treinando")

# funcao para converter listas em strings
def listToString(list):
    s = str(list).strip('[]')
    s = s.replace(' ', '')
    return s

# inicio do algoritmo
for k in range(1,max_int):
    acertos = 0    
    print("INTERACAO "+str(k)+"-------------------------")
    for i in range(0,len(x)):
        soma = 0
        
        # pega o nome da valvula no dicionário
        if d.has_key(listToString(x[i])):
            valvula = d[listToString(x[i])]  
        else:
            valvula = ""
            
        # para calcular a saida do adaline, cada entrada de x e multiplicada
        # pelo seu peso w correspondente
        for j in range(0,len(x[i])):
            soma += x[i][j] * w[j]

        # a saida e igual a soma anterior
        y_in = soma
        #print("y_in = ",str(y_in))        
                  

        # funcao de ativação
        if y_in >= 0:
            y = 1       
        else:
            y = -1
            
        # atualiza os pesos
        for j in range (0,len(w)):                
           # regra delta
           w[j] = w[j] + taxa_aprendizado * (t[i] - y_in) * x[i][j]
           print('Pesos Atualizados: %s' % w[j])        
        
        if y == t[i]:
            acertos+=1
            resposta = "acerto"
            #print('Quantidade de Acertos: %s | Quantidade X: %s' % (acertos, len(t)))
        else:
            resposta = "erro"
        
        #imprime a resposta
        if y == 1:
            print("Ativa Porta B = "+resposta)
        elif y == -1:
            print("Ativa Porta A = "+resposta)
            
        if acertos == len(t):
            print("Funcionalidade aprendida com "+str(k)+" interacoes")
            break
        print("")
print("Finished")