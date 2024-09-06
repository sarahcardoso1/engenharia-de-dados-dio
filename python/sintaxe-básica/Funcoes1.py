def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem2(nome):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem2("Sarah")


##-----------retorno

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

calcular_total([10, 20, 34])
retorna_antecessor_e_sucessor(10)

# -------- args e kwargs
 
 