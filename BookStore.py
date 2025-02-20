import Books
#No tocar clases Book y Users
class bookStore:
    def __init__(self, bookAdded):
        if isinstance(bookAdded, Books.book):  # Verifica que bookAdded es una instancia de Libro
            self.book = bookAdded
        else:
            raise TypeError("El objeto debe ser una instancia de la clase Libro")

        
        self.booksInventory={
            self.book.getIdBook() : [self.book.getNamBook(), self.book.getCategBook()]
        }

    def addBook(self, newBook):
        """Agrega un nuevo libro al inventario."""
        if isinstance(newBook, Books.book):
            self.booksInventory[newBook.getIdBook()] = [newBook.getNamBook(), newBook.getCategBook()]
        else:
            raise TypeError("El objeto debe ser una instancia de la clase Books.book")


    def deleteBook(self, bookId):
        if bookId in self.booksInventory:
            del self.booksInventory[bookId]
        else:
            return "Libro no esta en el inventario."