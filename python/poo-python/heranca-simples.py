class Veiculo: 
    def __init__(self, cor, placa, num_rodas):        
        self.cor = cor 
        self.placa = placa 
        self.num_rodas = num_rodas


    def ligar_motor(self):
        print("ligando o motor")

     def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([ f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, num_rodas, carregado):
        super().__init__(cor, placa, num_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'}")
    

moto = Motocicleta("preta", "abcd45", 2)
moto.ligar_motor()

carro = Carro("branco", "fgh-890", 4)
carro.ligar_motor()

caminhao = Caminhao("preto", "hjhj-0909", 8, False)
caminhao.ligar_motor()
caminhao.esta_carregado()
