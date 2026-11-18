from livros import Livro
from usuarios import Usuario
from emprestimos import Emprestimo

usuario = Usuario("Stênio", 123)
livro = Livro("Jogos Vorazes", "Não sei", 46)
emprestimo = Emprestimo("Jogos Vorazes", "Stênio")
print(f"Disponibilidade do livro após empréstimo: {livro.disponivel}")
emprestimo.devolver()

print(f"Disponibilidade do livro após devolução: {livro.disponivel}")