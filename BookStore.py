import Books

class bookStore:
    def __init__(self, bookAdded):
        if isinstance(bookAdded, Books.book):  # Verifica que bookAdded es una instancia de Libro
            self.book = bookAdded
        else:
            raise TypeError("El objeto debe ser una instancia de la clase Libro")


