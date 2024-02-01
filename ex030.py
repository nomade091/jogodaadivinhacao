from random import randint
from time import sleep

computador = randint(0, 5) # Gera um número aleatório entre 0 e 5

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

# Obtem a tentativa do jogador
try:
    jogador = int(input('Em que número eu pensei? '))
except ValueError:
    print('Por favor, digite um número válido.')
    exit()

print('PROCESSANDO...')
sleep(1)

# Verifica se o jogador acertou
if jogador == computador:
    print(f'PARÁBENS! Você conseguiu me vencer. Eu pensei no número {computador}.')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}!')
