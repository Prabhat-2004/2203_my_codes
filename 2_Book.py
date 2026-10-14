class Book:
    def is_borrowed(self):
        print(f"{self.title} has been marked as borrowed.")
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Status: {self.status}")
    
b1 = Book()
b2 = Book()
b1.author = "George Orwell"
b2.author = "George Orwell"
b1.title = 1984
b2.title = 1984
b1.status = "Available"
b2.status = "Borrowed"
b1.display_info()
b2.is_borrowed()
b2.display_info()