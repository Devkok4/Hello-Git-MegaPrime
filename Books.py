class Book:
    def __init__(self, namBook, idBook, catBook):
        self.namBook=namBook
        self.idBook=idBook
        self.catBook=catBook
    
    def getNameBook(self):
        return self.namBook
    
    def getCategBook(self):
        return self.catBook
    
    def getIdBook(self):
        return self.idBook
    
    def setNameBook(self, nameBook):
        self.namBook= nameBook
    
    def setCategBook(self, categBook):
        self.catBook= categBook
    
    def setIdBook(self, idBook):
        self.idBook= idBook
    