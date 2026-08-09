class Book:
    def __init__(self,book_id,title,author,category,quantity):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.category=category
        self.quantity=quantity
    def display(self):
        print(f"Book ID :{self.book_id}")    
        print(f"Title   :{self.title}")    
        print(f"Author  :{self.author}")  
        print(f"Category:{self.category}")    
        print(f"Quantity:{self.quantity}")    
    def issue_book(self):
        if self.quantity > 0:
           self.quantity -=1

           print("Book issued successfully")

        else:
            print("Book is not available")

    def return_book(self):
        self.quantity += 1
        print("Book returned successfully")
                  
b1=Book(2469,"Atomic habits","James clear","self help",205)
b1.display() 
b1.issue_book()
b1.return_book()
b1.display() 
      


