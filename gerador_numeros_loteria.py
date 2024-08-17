import random

print("Gerador de Jogos de loteria: \n")

numero_minimo = int(1)
numero_maximo = int(60)
array_jogos = []
indice_jogos = int(0)
indice_numeros = int(0)

qtd_jogos = int(input("Digite a quantidade de jogos: "))
qtd_numeros = int(input("Digite a quantidade de numeros por jogos: "))

print("\n")

for indece_jogos in range(qtd_jogos):
    array_jogos = []
    for indice_numeros in range(qtd_numeros):
        numero_sorteado = int(random.randrange(numero_minimo, numero_maximo))
        while numero_sorteado in array_jogos:
            numero_sorteado = int(random.randrange(numero_minimo, numero_maximo))
        array_jogos.append(numero_sorteado)
    print("Jogo " + str(indece_jogos) +  ": " + str(array_jogos))