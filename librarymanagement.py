from abc import ABC,abstractmethod
class Library(ABC):
    @abstractmethod
    def add_books(self):
        pass
    @abstractmethod
    def view_books(self):
        pass
    @abstractmethod
    def issue_books(self):
        pass
    def return_books(self):
        pass
    @abstractmethod
    def delete_books(self):
        pass
class College(Library):
    def __init__(self,books):
        self.books=books

    def check(self):
        print("Library Management")
    def add_books(self):
        if self.books==[]:
            count=int(input("\nHow many Books would you add:"))
            print("\nEnter Books name:")
            for i in range(count):
                bname=input()
                self.books.append(bname)
            print("Your Books is added")
        else:
            print("\nEnter Book Name:")
            self.books.append(input())
            print("Your Book is added")
    def view_books(self):
        print("\nList of Books:")
        for sno,name in enumerate(self.books,1):
            print("{}.{}".format(sno,name))
    def issue_books(self):
        ibook=input("\n Which Book you want to issue:")
        if ibook in self.books:
            self.books.remove(ibook)
            print("Book issued")
        else:
            print("Invalid Book name")
    def return_books(self):
        rbook=input("\n Which book would you return:")
        self.books.append(rbook)
        print("Book received")
    def delete_books(self):
        dbook=input("\n Which Book would you want to remove:")
        
        if dbook in self.books:
                self.books.remove(dbook)
                print("Your Book was  removed")
        else:
                print("Invalid Book name")
                
books=[]
obj=College(books)
obj.check()
                  
while True:
            
        print("\n")
        print("1.Add Books")
        print("2.View Book")
        print("3.Issue Book")
        print("4.Return Book")
        print("5.Delete Book")
        print("\n")
        data=int(input("\n Please Enter Your operation:"))
        if (data==1):
            obj.add_books()
        elif(data==2):
            obj.view_books()
        elif (data==3):
            obj.issue_books()
        elif (data==4):
            obj.return_books()
        elif (data==5):
            obj.delete_books()
else:
     print("exit")
     
                                    