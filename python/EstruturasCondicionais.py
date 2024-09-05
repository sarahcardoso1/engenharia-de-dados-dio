##### if

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH")

if idade >= MAIOR_IDADE: 
    print("Maior idade, pode tirar a CNH")
else: 
    print("Ainda não pode tirar a CNH")


#####--------------- elif 

if idade >= MAIOR_IDADE: 
    print("Maior idade, pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer as aulas práticas")
else: 
    print("Ainda não pode tirar a CNH")    


    ##### ----------------estrutura condicional aninhada (if aninhado)

conta_normal = True 

saldo = 2000
saque = 500
cheque_especial = 450 
conta_universitaria = 300

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque relizado com uso de cheque especial")
    else:
        print("Não foi possível realizar o saldo, saque insuficiente")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else: 
        print("Não foi possível realizar")
else: 
    print("Sistema não reconheceu o sue tipo de conta, entre em contato com o seu gerente")


###### ------------if ternário 

saldo = 2000
saque = 500


status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque")


