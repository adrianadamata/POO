# aluno.py

class Aluno:
    def __init__(self, nome, matricula, curso):
        self.__nome = nome
        self.__matricula = matricula
        self.__curso = curso
        self.__notas = []

    # Getter para o nome:
    def get_nome(self):
        return self.__nome

    # Getter para a matrícula
    def get_matricula(self):
        return self.__matricula

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.__notas.append(nota)

    def calcular_media(self):
        return sum(self.__notas) / len(self.__notas) if self.__notas else 0

    def mostrar_dados(self):
        print(f"Nome: {self.__nome} | Matrícula: {self.__matricula}")
        self.__curso.mostrar_detalhes()
        print(f"Média: {self.calcular_media():.2f}")
