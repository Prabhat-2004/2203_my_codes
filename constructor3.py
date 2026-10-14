class Book:
    def __init__(self, title, author, status):
        self.ttl = title
        self.aut = author
        self.sts = status

    def main(self):
        print(f"Title: {self.ttl}, Author: {self.aut}, Status: {self.sts}")
        if self.sts == "Available":
            print("is available")

b1 = Book(1984, "George Orwell", "Available")
b2 = Book(1984, "George Orwell", "Borrowed")

b1.main()
print()
b2.main()
