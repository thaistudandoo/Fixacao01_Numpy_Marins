#ATIVIDADE DE FIXAÇÃO 1 - Thaís Marins

import numpy as np

dados = np.genfromtxt('dados.txt', delimiter=' ')

#1) Criar um array bidimensional com dados diferentes dos utilizados em sala;

#array_bidimensional = [[22, 11, 98],[3,6,95],[24,28,23]]
array_bidimensional = np.array([[22, 11, 98],[3,6,95],[24,28,23]])
#array_bidimensional = dados
print(array_bidimensional)
thais = array_bidimensional[0,:]
mateus = array_bidimensional[1,:]
print(f"Dados Thaís:{thais}\nDados Mateus:{mateus}")

#2) Obter dados estatísticos diferentes (pelo menos 3, uma com axis=1, a outra com axis = 0 e a última sem axis);

#Média Linhas
media_linhas = np.mean(array_bidimensional, axis=1)
print(f"Média das linhas:{media_linhas}")

#Médias Colunas
media_colunas = np.mean(array_bidimensional, axis=0)
print(f"\nMédia das colunas:{media_colunas}")

#Média Total
media_total = np.mean(array_bidimensional)
print(f"Média total: {media_total:.2f}") 

#3) Obter a transposta da matriz e realizar uma operação com ela;
array_t = np.transpose(array_bidimensional)
print(array_t)

#Multiplicação por escalar
escalar = 5
array_t_escalar = escalar * array_t
print(array_t_escalar)

#Multiplicação de matrizes
produto_matriz = np.dot(array_bidimensional, array_t)
print(f"\n Produto da Matriz com a sua Transposta:\n{produto_matriz}")

#4) Realizar um produto escalar entre duas matrizes ou de um array com uma matriz;
produto = array_bidimensional @ array_t
print(f"\n Produto da Matriz com a sua Transposta utilizando o operador '@':\n{produto}")

#5)Criar um filtro para a sua matriz;

#Transformando o array bidimensional em matriz
matriz = np.array(array_bidimensional)
print(f"\nA matriz original é:\n{matriz}")

#Filtrando apenas os numeros pares
filtro = matriz % 2 == 0
print(f"\nFiltro criado para os número pares: \n{filtro}")

array_filtrado = matriz[filtro]

print(f"\nArray de número pares:{array_filtrado}")

#6)Realizar alguma operação aritmética (número com matriz, array com matriz, etc.);
matriz_t = matriz.T
print(f'Matriz transposta realizada com .T:\n {matriz_t}\n')

soma_matriz = matriz+matriz_t
print(f'Soma Matriz e Matriz transposta:\n {soma_matriz}\n')

soma_matriz2 = np.add(matriz, matriz_t)
print(f'Soma Matriz e Matriz transposta utilizando o método add:\n {soma_matriz2}\n')

sub_matriz = matriz-matriz_t
print(f'Subtração da Matriz e Matriz transposta:\n {sub_matriz}\n')

sub_matriz2 = np.subtract(matriz,matriz_t)
print(f'Subtração da Matriz e Matriz transposta utilizando o método subtract():\n {sub_matriz2}\n')


linhas, colunas = matriz.shape
print(f"Matriz {linhas} X {colunas}")

determinante = np.linalg.det(matriz)
print(f"Determinante da Matriz:{determinante}")

if determinante != 0:
    print("A matriz é inversível.")
else:
    print("A matriz não é inversível.")

matriz_inversa = np.linalg.inv(matriz)
print(f"Inversa:{matriz_inversa}")

#resultado = np.dot(matriz, matriz_inversa)
resultado = np.array(np.matmul(matriz, matriz_inversa), dtype=int)
print(f"Identidade: \n{resultado}")


# matriz_identidade = np.eye(linhas, colunas)

# Exibir a matriz identidade
# print("Matriz Identidade:")
# print(matriz_identidade)

#7)Vincular com o github (código deve estar no repositório sem o venv ou outros arquivos de configuração);





#EXTRA (200XP): Os dados devem vir de algum arquivo externo.