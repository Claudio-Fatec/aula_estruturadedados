"""
Programa simples que verifica o balanceamento  de parênteses em expressões 
matemáticas usando pilha
"""
from lib.stack import Stack

pilha = Stack()

# expr = "(2 * (3 + 4) - (5 / 3) + ) - 2"
# expr = "(2 * ((3 + 4) - ((5 / 3) + ) - 2"
expr = "(2 * (3 + 4)) - (5 / 3) + )) - 2"

for pos in range(len(expr)):
    # 1º PARTE: percorre a expressão e EMPILA as posições onde
    # são encontrados os caracteres de abre parênteses
    if expr[pos] == "(": pilha.push(pos)
    
    # 2º PARTE: ao encontrar um caractere de fecha parêntese,
    # tenta desempilhar
    elif expr[pos] == ")":
        # A pilha não pode esta vazia quando for encontrado um
        # fecha parêntese
        if pilha.is_empty():
            print(f"ERRO: parêntese fechado na posição {pos} não tem o abre correspondente")
        else:
            pos_emp = pilha.pop()
            print(f"Parêntese aberto na posição {pos_emp} foi fechado na posição {pos}.") 

# <~ CUIDADO COM A INDENTAÇÃO AQUI!
# Processa eventuais sobras na pilha após o término da
# análise da expressão
while not pilha.is_empty():
    pos_emp = pilha.pop()
    print(f"ERRO: parêntese aberto na posição {pos_emp} não tem o fecha correspondente")
    
print(pilha)