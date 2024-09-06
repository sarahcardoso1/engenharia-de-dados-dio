#tabela da verdade - 
## AND = para ser T tudo tem que ser T
## OR = para ser T tudo tem que ser T 

print(True and True)
print(True and False)
print(True or False)
print(True or True)

# exemplo simples 

saldo = 1000
saque = 200
limite = 100 

saldo >= saque and saque <= limite
saldo >= saque or saque <= limite


# operador de negação 

contatos_emergencia = []  #sequencia vazia é considerada falso 

not 1000 > 1500

not contatos_emergencia

not "saque 1500;"

not ""

# parênteses 

saldo = 1000
saque = 250
limite = 200
conta_especial = True 

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite)  
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)

