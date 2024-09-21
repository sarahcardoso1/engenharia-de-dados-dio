class Doguinhos:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado 

    def __del__(self):
        print("Removendo a instancia da classe")

    def falar(self):
        print("miau miau miau miau")

def criar_doguinho():
    c = Doguinho("freud", "branco", False)
    print(c.nome)

c = Doguinhos("Qwerty", "Caramelo")
c.falar()

del c 

print("oI DoguINHO")