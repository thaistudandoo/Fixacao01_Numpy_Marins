#ATIVIDADE DE FIXAÇÃO 01 - Numpy
#Por: Thaís Marins

import numpy as np

dados = np.genfromtxt('dados.txt', delimiter=' ')

#1) Criar um array bidimensional com dados diferentes dos utilizados em sala;

array_bidimensional = np.array([[22, 11, 98],[3,6,95],[24,28,23]])

#Para realizar as tarefas usando dados do arquivo externo basta excluir o '#' da linha seguinte(13).
array_bidimensional = dados
print(f"\nArray Bidimensional:\n{array_bidimensional}")

thais = array_bidimensional[0,:]
mateus = array_bidimensional[1,:]
print(f"\nDados Thaís:{thais}\nDados Mateus:{mateus}")
#__________________________________________________________________________________________________________________
#2) Obter dados estatísticos diferentes (pelo menos 3, uma com axis=1, a outra com axis = 0 e a última sem axis);

#Soma Linhas
soma_linhas = np.sum(array_bidimensional, axis=1)
print(f"\nSoma das linhas:{soma_linhas}")

#Soma Colunas
soma_colunas = np.sum(array_bidimensional, axis=0)
print(f"Soma das colunas:{soma_colunas}")

#Soma Total
soma_total = np.sum(array_bidimensional)
print(f"Soma Total:{soma_total}")

#Média Linhas
media_linhas = np.mean(array_bidimensional, axis=1)
print(f"\nMédia das linhas:{media_linhas}")

#Médias Colunas
media_colunas = np.mean(array_bidimensional, axis=0)
print(f"\nMédia das colunas:{media_colunas}")

#Média Total
media_total = np.mean(array_bidimensional)
print(f"Média Total:{media_total:.2f}")

#MedianaTotal
mediana_total = np.median(array_bidimensional)
print(f"\nMediana Total:{mediana_total:.2f}")


#__________________________________________________________________________________________________________________
#3) Obter a transposta da matriz e realizar uma operação com ela;
array_t = np.transpose(array_bidimensional)
print(f"\nMatriz Transposta:\n{array_t}")

#Multiplicação por escalar
escalar = 5
array_t_escalar = escalar * array_t
print(f"\nMatriz transposta * {escalar}:\n{array_t_escalar}")

#Multiplicação de matrizes
produto_matriz = np.dot(array_bidimensional, array_t)
print(f"\n Produto da Matriz com a sua Transposta:\n{produto_matriz}")

#__________________________________________________________________________________________________________________
#4) Realizar um produto escalar entre duas matrizes ou de um array com uma matriz;
array_produto = np.array([2, 4, 6])
produto_array = array_bidimensional @ array_produto
print(f"\n Produto da Matriz com um array: {produto_array}")

produto_matriz = array_bidimensional @ array_t
print(f"\n Produto da Matriz com a sua Transposta utilizando o operador '@':\n{produto_matriz}")

#__________________________________________________________________________________________________________________
#5)Criar um filtro para a sua matriz;

matriz = np.array(array_bidimensional)
print(f"\nA matriz original é:\n{matriz}")

#Filtrando apenas os numeros pares
filtro = matriz % 2 == 0
print(f"\nFiltro criado para os número pares: \n{filtro}")

array_filtrado = matriz[filtro]
print(f"\nArray de número pares: {array_filtrado}\n")

#__________________________________________________________________________________________________________________
#6)Realizar alguma operação aritmética (número com matriz, array com matriz, etc.);
matriz_t = matriz.T
print(f'\nMatriz transposta realizada com .T:\n {matriz_t}\n')

soma_matriz = matriz+matriz_t
print(f'\nSoma Matriz e Matriz transposta:\n {soma_matriz}\n')

soma_matriz2 = np.add(matriz, matriz_t)
print(f'\nSoma Matriz e Matriz transposta utilizando o método add:\n {soma_matriz2}\n')

sub_matriz = matriz-matriz_t
print(f'\nSubtração da Matriz e Matriz transposta:\n {sub_matriz}\n')

sub_matriz2 = np.subtract(matriz,matriz_t)
print(f'\nSubtração da Matriz e Matriz transposta utilizando o método subtract():\n {sub_matriz2}\n')

linhas, colunas = matriz.shape
print(f"\nMatriz {linhas} X {colunas}")

det = np.linalg.det(matriz)
print(f"\nDeterminante da Matriz:{det}")

if det != 0:
    print("\nA matriz é inversível! :)")
else:
    print("\nA matriz não é inversível! :(")

matriz_inversa = np.linalg.inv(matriz)
print(f"\n Matriz Inversa:\n{matriz_inversa}")

#resultado = np.dot(matriz, matriz_inversa)
#id = a * a^-1
resultado = np.array(np.matmul(matriz, matriz_inversa), dtype=int)
print(f"\n Resultado da operação é a Matriz Identidade: \n{resultado}")

#__________________________________________________________________________________________________________________
#7)Vincular com o github (código deve estar no repositório sem o venv ou outros arquivos de configuração);
# Feito :)

#EXTRA (200XP): Os dados devem vir de algum arquivo externo.
# Para conferir basta apagar o símbolo '#' da linha 13 ("array_bidimensional = dados")
