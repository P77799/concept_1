class Library:
    def __init__(self,name):
        self.name=name
        self.books=["python1010","Java basic","novels","poems","science books","Data science book"]

    def display(self):
            print(f"the books available in library are{self.books} :")

    def add(self,book):
            self.books.append(book)
            print(f"you have added {book} in library ")

    def lend(self,lend_book):
            if lend_book in self.books:
                self.books.remove(lend_book)
                print(f"you have Lend  {lend_book} from Library")
            else:
                 print(" Book not available")

    def returns(self,return_book):
            
            self.books.append(return_book)
            print(f"u have return {return_book}")




def main():

    Li=Library("Pratik_library")


    while True:
        print("LIBRARY MENUE")
        print("1 Display")
        print("2 Add")
        print("3 Lend book")
        print("4 Return BOOK")
        print(" 5 exite")

        choice =int(input("Enter the num from 1-5 : "))



    
   

        if choice==1:
            Li.display()

        elif choice==2:
            book=input("Enteer the name of the book u wanna add :")
            Li.add(book)
        
        elif choice==3:
            lend_book=input("Enter the name of the book u wanna lend from library :")
            Li.lend(lend_book)

        elif choice==4:
            return_book=input("Enter the name of the book u return: ")
            Li.returns(return_book)

        elif choice==5:
            print("exit thanks for using Pratik library!!")
            
        else:
            print("invalidddddddddd num")

main()




