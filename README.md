# Modularização em Python: Projeto POO com Composição

Neste notebook, vamos aprender a:
- Criar e organizar módulos em Python
- Separar classes em arquivos diferentes
- Importar e reutilizar código no Jupyter Notebook

## 📁 Estrutura modular sugerida

- `aluno.py`: Contém a classe `Aluno` e suas subclasses (`AlunoIntegrado`, `AlunoGraduacao`, etc.)
- `curso.py`: Contém a classe `Curso`
- `utilidades.py`: Contém funções auxiliares (ex: entrada de nota)
- `main.ipynb`: Este notebook que importa os módulos e executa o programa principal
