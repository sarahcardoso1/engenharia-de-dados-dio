class Animal:
    def __init__(self, num_patas ):
        self.num_patas = num_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([ f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw ):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

    def __str__(self):
        return self.__class__.__name__

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class FalarMixin:
    def falar(self):
        return"hablo"


class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Onitorrinco(Mamifero, Ave):
     def __init__(self, cor_bico, cor_pelo, num_patas):
        print(Onitorrinco.__mro__)

        super().__init__(cor_bico = cor_bico, cor_pelo=cor_pelo, num_patas=num_patas)


gato = Gato(num_patas=4 ,cor_pelo='siameso')
print(gato)

Onitorrinco = Onitorrinco(num_patas= 2, cor_pelo="azul", cor_bico="amarelo")
print(Onitorrinco)
print(Onitorrinco.falar())