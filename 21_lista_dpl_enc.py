from lib.doubly_linked_list import DoublyLinkedList

lista = DoublyLinkedList()

print(lista)

lista.insert(0, 'manga')

print(lista)

lista.insert(1,'abacaxi')

print(lista)

lista.insert(2,'caju')
lista.insert(3,'laranja')
lista.insert(4,'maçã')

print(lista)

lista.insert(3,'banana')

print(lista)

# Mais algumas inserções
lista.insert(0,'uva')
lista.append('morango')
lista.append('mamão')

print(lista)

#Fazendo algumas consultas
primeira = lista.peek(0)
pos5 = lista.peek(5)
ultima = lista.peek(-1)
penultima = lista.peek(-2)

print(f"PRIMEIRA FRUTA: {primeira}; FRUTA NA POS. 5:{pos5}; ÚLTIMA: {ultima}; PENÚLTIMA: {penultima}")

print(lista)

# Fazendo remoções
rem_primeira = lista.remove(0)
print(f"Fruta removida de primeira posição: {rem_primeira}")

rem_ultima = lista.pop()  # equevalente a lista.remove(lista.count() -1)
print(f"Frutaremovida da últma posição: {rem_ultima}")

print(lista)

rem_pos3 = lista.remove(3)
print(f"Fruta removidada posição 3: {rem_pos3}")

print(lista)

print(f"Quantidade finalde itens na lista: {lista.count()}")