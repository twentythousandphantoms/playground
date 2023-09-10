# Challenge:
# Given a class that represents a Book with various properties such
# as author, title, price, etc.
# 1) Implement the __repr__ and __str__ methods to output:
#    str: "(title) by (author): (pagecount), (cover), (price)"
#    repr: "<Book:title:author:pages:cover:antique:genre:price>"
# 2) Implement the comparison methods so that books can be compared based on pagecount.
# 3) Implement the enum that represents the type of the book cover. The allowable values are:
#    HARDCOVER, PAPERBACK. Replace the cover property with a property that uses the enum.
# 4) Implement the "adjustedprice" computed property - books that are antiques have a 10.00 surcharge
#    added to the price, Paperbacks have a 2.00 discount, and the rest have no surcharge.
# 5) Successfully execut the sample code provided below.


class Book():
    def __init__(self, title, author, pages, cover, antique, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.cover = cover
        self.antique = antique
        self.price = price

    # TODO: Implement the str and repr functions
    def __str__(self):
        return f"{self.title} by {self.author}: {self.pages}, {self.cover}, {self.price}"

    def __repr__(self):
        return f"<Book:{self.title}:{self.author}:{self.pages}:{self.cover}:{self.antique}:{self.price}>"

    # TODO: Implement the adjustedprice attribute
    @property
    def adjustedprice(self):
        if self.antique:
            return self.price + 10.00
        elif self.cover == "Paperback":
            return self.price - 2.00
        else:
            return self.price

    # TODO: Implement comparisons <, >, <=, >=
    def __lt__(self, other):
        return self.pages < other.pages

    def __gt__(self, other):
        return self.pages > other.pages

    def __le__(self, other):
        return self.pages <= other.pages

    def __ge__(self, other):
        return self.pages >= other.pages

# TODO: Implement the Hard/Paperback Enum
from enum import Enum, auto

class Cover(Enum):
    HARDCOVER = "Hardcover"
    PAPERBACK = "Paperback"



books = [
    Book("War and Peace", "Leo Tolstoy", 1225, Cover.HARDCOVER, True, 29.95),
    Book("Brave New World", "Aldous Huxley", 311, Cover.PAPERBACK, True, 32.50),
    Book("Crime and Punishment", "Fyodor Dostoevsky", 492, Cover.HARDCOVER, False, 19.75),
    Book("Moby Dick", "Herman Melville", 427, Cover.PAPERBACK, True, 22.95),
    Book("A Christmas Carol", "Charles Dickens", 66, Cover.HARDCOVER, False, 31.95),
    Book("Animal Farm", "George Orwell", 130, Cover.PAPERBACK, False, 26.95),
    Book("Farenheit 451", "Ray Bradbury", 256, Cover.HARDCOVER, True, 28.95),
    Book("Jane Eyre", "Charlotte Bronte", 536, Cover.PAPERBACK, False, 34.95)
]

# TEST CODE

# 1 - test the str and repr functions
print("-------------")
print(str(books[0]))
print(str(books[3]))
print(str(books[5]))
print()
print(repr(books[0]))
print(repr(books[3]))
print(repr(books[5]))
print("-------------")

# 2 - test the "adjustedprice" computed attribute
for book in books:
    print(f"{book.title}: {book.adjustedprice:.2f}")
print("-------------")
print()

# 3 - compare on pagecount
print(books[1] > books[2])
print(books[4] < books[6])
print(books[7] >= books[0])
print(books[3] <= books[4])
