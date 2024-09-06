

nome = "Guilherme"
idade = 28
profissao = "programador"
linguagem = "python"

print("Ola eu sou %s. Tenho %d anos e trabalho como %s." % (nome, idade, profissao))



#--------- metodo format 

nome = "Guilherme"
idade = 28
profissao = "programador"
linguagem = "python"

print("Ola eu sou {}. Tenho {} anos e trabalho como {}." .format(nome, idade, profissao))

print("Ola eu sou {2}. Tenho {1} anos e trabalho como {0}." .format(profissao, idade, nome))


#--------- f-string

nome = "Guilherme"
idade = 28
profissao = "programador"
linguagem = "python"

print("Ola eu sou {nome}. Tenho {idade} anos e trabalho como {profissao}.")



#--------- formatar com f-string

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")



