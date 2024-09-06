# ------------- parametros posicionais 

def criar_carro(modelo, ano, placa, / , marca, motor, combustivel):
    print(modelo, ano, placa, marca, combustivel, motor)

criar_carro("Ferrari 250", 1999, "ABC-8790", "Ferrari", "V12", "Gasolina")


# ------------- parametros por nome 

# def criar_carro(*modelo, ano, placa, marca, motor, combustivel):
   # print(modelo, ano, placa, marca, combustivel, motor)

#criar_carro(modelo="Ferrari 250", ano=1999, placa="ABC-8790", marca="Ferrari", motor="V12", combustivel="Gasolina")


# ------------- parametros posicionais e nomeados 

# junção de ambos 


# ------------- objetos de primeira classe

def somar(a,b):
    return a + b

def subtrair(a, b):
    return a - b



def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operaçao é = {resultado}")

exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)

op = somar
print(op(1, 23))


# ------------- escopos globais e locais 

salario = 2000

def salario_bonus(bonus):
    global salario


    lista.append(2)
    salario += bonus
    return salario


lista = [1]
salario_bonus = salario_bonus(500, lista )
print(salario_bonus)
print(lista)