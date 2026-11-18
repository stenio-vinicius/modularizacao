from livros import Livro
from usuarios import Usuario

class Emprestimo:
    def __init__(self, livro, usuario, ativo = True):
        self.livro = Livro
        self.usuario = Usuario
        self.ativo = ativo

    @property
    def livro(self):
        return self.livro

    @livro.setter
    def livro(self, novo):
        if novo.disponivel == False:
            raise ValueError
        self.livro = novo
        self.livro.disponivel = False

    def devolver(self):
        self.ativo = False
        self.livro.disponivel = True