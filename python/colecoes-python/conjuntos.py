numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)

fruta = set("abacaxi")
print(fruta)


linguagens = {"python", "java", "python"}
print(linguagens)

#----------------- conjuntos não suportam indexação nem slicing[:1]

#{}.union #(todos os elementos juntos)

conjunto_a = {1,2}
conjunto_b = {3,4}
conjunto_a.union(conjunto_b)

#----------------

#{}.intersection #pontos ou dados em comum

conjunto_a = {1,2,4}
conjunto_b = {3,4}
conjunto_a.intersection(conjunto_b)

#----------------

#{}.difference #o que está em um e não está n outro

conjunto_a = {1,2,4}
conjunto_b = {3,4}

conjunto_a.difference(conjunto_b)
conjunto_b.difference(conjunto_a)

#----------------

#{}.symmetric_difference  #não se tocam, dados diferentes

conjunto_a = {1,2,4}
conjunto_b = {3,4}

conjunto_a.symmetric_difference(conjunto_b)

#----------------

#{}.issubset  #

conjunto_a = {1,2,4}
conjunto_b = {3, 4, 1, 5, 6, 7, 9}

conjunto_a.issubset(conjunto_b)
conjunto_b.issubset(conjunto_a)

#----------------

#{}.issuperset 

conjunto_a = {1,2,4}
conjunto_b = {3, 4, 1, 5, 6, 7, 9}

conjunto_a.issuperset(conjunto_b)
conjunto_b.issuperset(conjunto_a)

#----------------

#{}.isdisjoint

conjunto_a = {1,2,4}
conjunto_b = {3, 4, 1, 5, 6, 7, 9}
conjunto_c = {1,0}

conjunto_a.isdisjoint(conjunto_b)
conjunto_a.isdisjoint(conjunto_c)


#----------------

# {}.add  se passar elemento que já existe, será ignorado

numeros = {1, 23}

numeros.add(44)
numeros.add(49)

#----------------

#{}.clear
#{}.copy

#----------------

#{}.discard

numeros = {1, 2, 3, 4, 5, 6, 7, 8}

numeros.discard(4)

#----------------

#{}pop

numeros = {1, 2, 3, 4, 5, 6, 7, 8}

print(numeros.pop())

#----------------

#{}.remove      se o elemento não existe, retorna erro

numeros = {1, 2, 3, 4, 5, 6, 7, 8}

print(numeros.remove(4))

#----------------

#in

numeros = {1, 2, 3, 4, 5, 6, 7, 8}

1 in numeros
10 in numeros 









