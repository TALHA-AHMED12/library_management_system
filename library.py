print("\n" + "="*50)
print("📚 WELCOME TO THE LIBRARY MANAGEMENT SYSTEM 📚")
print("="*50 + "\n")

booklist = []
matchingBook = []

while True:
    print('\n'+'-'*40)
    print('🔍 MAIN MENU')
    print('-'*40)
    print('1. 📋 Display all books')
    print('2. ➕ Add a book')
    print('3. ❌ Remove a book')
    print('4. 🔍 Search for a book')
    print('5. 📊 Display statistics')
    print('6. 🚪 Exit')
    print('-'*40)
    decision = input('Enter your choice: ')

    if decision == '1':
        if len(booklist) == 0:
            print("\n❌ No books in the library")
        else:
            print("\n📚 LIST OF ALL BOOKS 📚")
            print("="*40)
            for i, book in enumerate(booklist, 1):
                print(f"\n📖 Book {i}:")
                print("│ Title   : " + book['Title'])
                print("│ Author  : " + book['Author'])
                print("│ Year    : " + str(book['Year']))
                print("│ Genre   : " + book['Genre'])
                print("│ Read    : " + ("✅" if book['Read This book?'].lower() == 'y' else "❌"))
                print("─"*40)
    elif decision == '2':
        book = {
            'Title': input('Enter the title: ').capitalize(),
            'Author': input('Enter the author: ').title(),  # Changed from capitalize() to title()
            'Year': int(input('Enter the year: ')),
            'Genre': input('Enter the genre: ').capitalize(),
            'Read This book?': input('Have you read this book? (y/n): ')
        }
        booklist.append(book)
        print('Book added successfully')
        continue
    elif decision == '3':
        removeBook = input('Enter the title of the book you want to remove: ').capitalize()
        book_found = False  # Initially set to False - assumes book is not found
        for book in booklist[:]:  # Create a copy of the list to iterate
            if book['Title'] == removeBook:
                booklist.remove(book)
                print('Book removed successfully')
                book_found = True  # Set to True when book is found and removed
                break
        if not book_found:  # If book was never found, inform the user
            print('Book not found')
        continue

        
    elif decision == '4':
        print('\n📍 Search for a book by its:')
        print('1. 📖 Title')
        print('2. ✍️ Author name')
        searchDecision = input('Enter your choice: ')
        if searchDecision == '1':
            searchTitle = input('Enter the title of the book: ').capitalize()
            matchingBook.clear()  # Clear previous search results
            book_found = False
            for book in booklist:
                if searchTitle in book['Title']:  # Changed comparison direction
                    matchingBook.append(book)
                    print('Matching book found:')
                    print('-------------------')
                    print(book)  # Print the book directly instead of the list
                    book_found = True
            if not book_found:
                print('Book not found')
            continue
        elif searchDecision == '2':
            searchAuthor = input('Enter the author of the book: ').title()  # Changed from capitalize() to title()
            matchingBook.clear()  # Clear previous search results
            book_found = False
            for book in booklist:
                if searchAuthor in book['Author']:
                    matchingBook.append(book)
                    print('Matching book found:')
                    print('-------------------')
                    print(book)
                    book_found = True
            if not book_found:
                print('Book not found')
            continue
        else:
            print('Invalid choice. Please try again.')
        continue

    elif decision == '5':
        print('\n📊 LIBRARY STATISTICS 📊')
        print('─'*40)
        print(f'📚 Total books in library: {len(booklist)}')
        if len(booklist) > 0:
            read_percent = (len([book for book in booklist if book['Read This book?'].lower() == 'y']) / len(booklist)) * 100
            print(f'✅ Books read: {read_percent:.1f}%')
            print(f'❌ Books not read: {(100-read_percent):.1f}%')
        print('─'*40)

    elif decision == '6':
        print('\n👋 Thank you for using the Library Management System!')
        print('📚 Library saved successfully. Goodbye! ✨')
        break

    else:
        print('\n❌ Invalid choice. Please try again.')

