pessoa = {"nome": "Sarah", "idade": 21}
pessoa = dict(nome="Guilherme", idade = 28)
pessoa["telefone"] = "33556-9898" 


#--------------------------acesso aos dados
dados = {"nome": Sarah, "idade": 21, "telefone": "33556-9898"}

dados["nome"]
dados["idade"]

dados["nome"] = "Maria"     #faz a substituição
dados["idade"] = 34



#-------------------------- dicionários aninhados    (estrutura dentro da outra)
contatos = {

    "email@exemplo.com":{"nome": "Sarah", "telefone": "33556-9898"},
    "email@2.com":{"nome": "Sarah", "telefone": "33556-9898"},

}

contatos["email@2.com"]["telefone"]                       # 1 argumento acessa o dicionário, 2 argumento acessa a chave




#-------------------------- iterar dicionários
for chave, valor in contatos.items():
    print(chave, valor)