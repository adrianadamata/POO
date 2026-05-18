# curso.py

class Curso:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def descricao(self):
        print(f"Curso: {self.nome} - Duração: {self.duracao} semestres")
