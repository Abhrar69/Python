library = []

while True:
    print("1. Add book")
    print("2. Display book")
    print("3. Update book")
    print("4. Delete book")

    a = int(input("Enter the choice: "))

    if a == 1:
        id = input("Enter the Book ID: ")
        name = input("Enter the Book Name: ")
        price = input("Enter the Book Price: ")
        author = input("Enter the Book Author Name: ")
        publisher = input("Enter the Book Publisher: ")

        list1 = [id, name, price, author, publisher]
        library.append(list1)

    elif a == 2:
        for i in library:
            print("1.Book ID: ", i[0])
            print("2.Book Name: ", i[1])
            print("3.Book Price: ", i[2])
            print("4.Author: ", i[3])
            print("5.Publisher: ", i[4])
            print("---------------------")
            print("----Another Book-----")
            print("---------------------")

    elif a == 3:
        book_id = input("Enter the Book ID to update: ")

        for i in library:
            if i[0] == book_id:
                print("1. Update Book ID")
                print("2. Update Book Name")
                print("3. Update Book Price")
                print("4. Update Book Author")
                print("5. Update Book Publisher")

                choice = int(input("Enter the field number to update: "))

                if choice == 1:
                    new_id = input("Enter the new Book ID: ")
                    i[0] = new_id
                elif choice == 2:
                    new_name = input("Enter the new Book Name: ")
                    i[1] = new_name
                elif choice == 3:
                    new_price = input("Enter the new Book Price: ")
                    i[2] = new_price
                elif choice == 4:
                    new_author = input("Enter the new Book Author: ")
                    i[3] = new_author
                elif choice == 5:
                    new_publisher = input("Enter the new Book Publisher: ")
                    i[4] = new_publisher

                print("Book information updated successfully!")   
            else:
                print("Book ID not found.")

    elif a == 4:
        book_id = input("Enter the Book ID to delete: ")
        for i in library:
            if i[0] == book_id:
                library.remove(i)
                print("Book deleted successfully!")
                break
        else:
            print("Book ID not found.")