from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property    
    @abstractproperty    
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")
        print("Ligado :)")
    
    def desligar(self):
        print("Desligando a TV..")
        print("Desligado!")

    @property
    def marca(self):
        return "Philco"

class ControleAC(ControleRemoto):
    def ligar(self):
        print("Ligando o AC")
        print("Ligado :)")

    def desligar(self):
        print("Desligando o AC..")
        print("Desligado!")
    
    @property
    def marca(self):
        return "LG"

    


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleAC()
controle.ligar()
print(controle.marca)