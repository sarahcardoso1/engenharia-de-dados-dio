class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome 
        self.matricula = matricula 

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Gio", 2)

mostrar_valores(aluno_1, aluno_2)


Estudante.escola = "Adventista"
aluno_1.escola = "Objetivo"
aluno_3 = Estudante("Noah", 3)
aluno_1.matricula = 3
mostrar_valores(aluno_1, aluno_2)
mostrar_valores(aluno_3)