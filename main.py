from library import Library, Book

if __name__ == "__main__":
    library = Library()

    print("Por favor, insira os dados dos livros: ")

    while True:
        title = input("Título: ")
        genre = input("Gênero: ")
        subgenre = input("Subgênero: ")
        publisher = input("Editora: ")

        while True:
            try:
                price = float(input("Preço: ").replace(",", "."))
                break
            except ValueError:
                print("Preço Inválido. Insira novamente.")

        book = Book(title, genre, subgenre, publisher, price)

        library.add(book)

        end = input("Deseja adicionar outro livro? S/N ").lower()
        if end == "n":
            break

    library.display()

    # APENAS PARA TESTE, NÃO FAZ PARTE DA SOLUCÃO. :)
    # harry_potter = Book("harry potter I", "acao", "aventura", "pascoal", 29.90)
    # harry_potter2 = Book("harry potter I", "ficcao", "aventura", "pascoal", 29.90)
    # harry_potter3 = Book("harry potter I", "acao", "aventura", "pascoal", 29.90)
    # selecao = Book("selecao", "romance", "epoca", "pascoal", 39.90)
    # escolha = Book("escolha", "romance", "epoca", "pascoal", 49.90)
    # escola2 = Book("escolha", "romance", "epoca", "pascoal", 49.90)
    # star_wars = Book("star wars illustration", "art", "illustration", "mediaval", 79.90)
    #
    # for book in [harry_potter, harry_potter2, harry_potter3, selecao, escolha, escola2, star_wars]:
    #     library.add(book)
    #
    # print(library.get_books("harry potter I", "acao", "aventura"))
