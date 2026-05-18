# cadastro.py

from curso import Curso
from aluno import Aluno


def cadastrar_cursos():
    cursos = []
    quantidade = int(input("Quantos cursos deseja cadastrar? "))

    for i in range(quantidade):
        print(f"\n📘 Cadastro do curso {i+1}")
        nome = input("Nome do curso: ")
        duracao = int(input("Duração (em semestres): "))
        cursos.append(Curso(nome, duracao))

    return cursos


def cadastrar_alunos(cursos):
    alunos = []
    quantidade = int(input("\nQuantos alunos deseja cadastrar? "))

    for i in range(quantidade):
        print(f"\n📌 Cadastro do aluno {i+1}")
        nome = input("Nome: ")
        matricula = input("Matrícula (8 a 10 dígitos): ")

        while True:
            escolha = input("Digite o número do curso: ")
            if escolha.isdigit() and 1 <= int(escolha) <= len(cursos):
                curso_escolhido = cursos[int(escolha) - 1]
                break
            else:
                print("⚠️ Escolha inválida.")

        aluno = Aluno(nome, matricula, curso_escolhido)
        alunos.append(aluno)

    return alunos


def adicionar_notas(alunos):
    for aluno in alunos:
        print(f"\nAdicionando notas para {aluno.get_nome()}:")
        for i in range(2):
            # O programa entra em um estado de "espera" e só sairá dele (através do comando break)
            while True:
                entrada = input(
                    f"Digite a nota {i+1} para {aluno.get_nome()}: ")
                if entrada.strip() == "":
                    print("⚠️ Entrada vazia. Digite uma nota válida.")
                    continue
                try:
                    nota = float(entrada)
                    if 0 <= nota <= 10:
                        aluno.adicionar_nota(nota)
                        break
                    else:
                        print("⚠️ A nota deve estar entre 0 e 10.")
                except ValueError:
                    print("⚠️ Valor inválido. Digite um número.")
