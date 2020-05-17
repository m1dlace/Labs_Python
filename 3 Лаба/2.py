from abc import abstractmethod

class Taggable:
    @abstractmethod
    def tag(self):
        pass

class Book(Taggable):
    count = 0
    def __init__(self, author, name):
        Book.count += 1
        self._name = name
        self._author = author
        self._code = Book.count

    def tag(self):
        words = self._name.split()
        return [word for word in words if word.istitle()]
    def __str__(self):
        return "[%d] %s '%s'" % (self._code, self._author, self._name)

class Library(object):
    def __init__(self, number, adress):
        self._adress = adress
        self._number = number
        self._books = []

    def __add__(self, book):
        self._books += [book]
        return self

    def __iadd__(self, book):
        return self.__add__(book)

    def __iter__(self):
        for book in self._books:
            yield book

lib = Library(1, '51 Some str., NY')
lib += Book('Leo Tolstoi', 'War and Peace')
lib += Book('Charles Dickens', 'David Copperfield')
for book in lib:
    print(book)
    print(book.tag())