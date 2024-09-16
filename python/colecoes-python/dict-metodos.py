#      {}.copy
#      {}.fromkeys

dict.fromkeys(["nome", "telefone"])
dict.fromkeys(["nome", "telefone"], "vazio")            #adicionar novas chaves de 1 vez só no dict 



#-------------------------- {}.get
contatos = {
    "email@exemplo.com":{"nome": "Sarah", "telefone": "33556-9898"},
    "email@2.com":{"nome": "Sarah", "telefone": "33556-9898"},
}

contatos.get("chave")
contatos.get("chave", {})                               #se não encontrar, retorna um dicionario vazio




#-------------------------- {}.items
contatos.items()                                        #retorna a lista de tuplas


#--------------------------
resultado = contatos.keys()                             #retorna só o valor das chaves 
print(resultado)


#--------------------------
resultado = contatos.pop("email@exemplo.com", {})       #remove e retorna o 2 argumento 
print(resultado)


#--------------------------
contatos.popitem()


#--------------------------
contatos.setdefault("nome", "Giovana")                   #caso não exista, automaticamente adiciona esses valores 
print(contatos)

#--------------------------
contatos.update()                                       #update com chaves que existem vão atualizar os valores originais, updates com 


#--------------------------
contatos.values()                                       #retorna somente os valores


#--------------------------

del contatos["email@exemplo.com"]["telefone"]           #apaga chave 
                                                        #sem os argumentos apaga todos os contatos

#--------------------------