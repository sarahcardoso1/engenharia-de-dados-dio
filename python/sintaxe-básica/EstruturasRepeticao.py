##### for/else

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:                            #utilizando um iterável
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()


##### range 

for numero in range(0, 11):
    print(numero, end=" ")


for numero in range(0, 51, 5):
    print(numero, end="")     


##### while 

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo extrato...")
else: 
    print("Obrigado por usar nosso sistema bancário, até logo!")



######### break 



while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break
   
    print(numero)

#for numero in range(100):

#  if numero % 2 == 0:
#       continue

#  print(numero, end=" ")

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
       continue

 