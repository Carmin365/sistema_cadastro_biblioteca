class Book:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

books = []

def cadastra_livro(titulo, autor, genero, quantidade):
    new_livro = Book(titulo, autor, genero, quantidade)
    books.append(new_livro)

def listar_books():
    for book in books:
        print(f'Título: {book.titulo}, Autor: {book.autor}, Gênero: {book.genero}, Quantidade: {book.quantidade}')

def buscar_book(titulo):
    for book in books:
        if book.titulo.lower() == titulo.lower():
            return book
    return None

pip install matplotlib

import matplotlib.pyplot as plt

def gerar_graphic():
    generos = {}
    for book in books:
        if book.genero in generos:
            generos[book.genero] += book.quantidade
        else:
            generos[book.genero] = book.quantidade

    plt.bar(generos.keys(), generos.values())
    plt.xlabel('Gênero')
    plt.ylabel('Quantidade de Livros')
    plt.title('Quantidade de Livros por Gênero')
    plt.show()

# Cadastrar alguns livros
cadastra_livro('Livro A', 'Autor A', 'Ficção', 10)
cadastra_livro('Livro B', 'Autor B', 'Não-Ficção', 5)
cadastra_livro('Livro C', 'Autor C', 'Ficção', 7)

# Listar todos os livros
listar_books()

# Buscar um livro pelo título
book = buscar_book('Livro A')
if book:
    print(f'Livro encontrado: {book.titulo}, Autor: {book.autor}, Gênero: {book.genero}, Quantidade: {book.quantidade}')
else:
    print('Livro não encontrado')

# Gerar gráfico da quantidade de livros de por gênero
gerar_graphic()