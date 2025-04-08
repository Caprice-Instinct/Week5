#   Created a class Book
class Book:
    # Attributes
    def __init__(self, genre, author, pages):
        self.genre = genre
        self.author = author
        self.__pages = pages    # Private Attribute
        
    # Methods
    def publish(self):
        print("Book got published")
        
     # Getter for pages (access the private attribute)
    def get_pages(self):
        return self.__pages

    # Setter for pages (modify the private attribute)
    def set_pages(self, pages):
        if pages > 0:
            self.__pages = pages
        else:
            print("Pages must be greater than 0.")    
        
        
# Use of constructors to initialise objects
encyclopedia = Book("Knowledge", "Einstein", 500)
print(encyclopedia.author)
encyclopedia.publish()
        
kidagaa = Book("Setbook", "Chazima", 150)
kidagaa.publish()

# Inheritance and Polymorphism
class Textbook(Book):
    def publish(self):
        print("Textbook published")
        
fundamentals_of_programming = Textbook("Programming", "Dr Lee", 300)
fundamentals_of_programming.publish()
print(fundamentals_of_programming.author)

# Encapsulation
fundamentals_of_programming.set_pages(3500)
print(f"Updated pages in the textbook: {fundamentals_of_programming.get_pages()}")