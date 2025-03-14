# 📚 Library Management System

A simple command-line library management system written in Python that helps users maintain and organize their book collection.

## 🌟 Features

- **Display Books**: View all books with detailed information
- **Add Books**: Add new books with title, author, year, genre, and reading status
- **Remove Books**: Remove books from the library by title
- **Search Books**: Search for books by:
  - 📖 Title
  - ✍️ Author
- **Statistics**: View library statistics including:
  - Total number of books
  - Percentage of books read/unread

## 📋 Book Information Stored

Each book entry contains:
- Title
- Author
- Publication Year
- Genre
- Reading Status (Read/Unread)

## 🚀 How to Use

1. Run the program: `python library.py`
2. Choose from the following options:
   - 1️⃣ Display all books
   - 2️⃣ Add a book
   - 3️⃣ Remove a book
   - 4️⃣ Search for a book
   - 5️⃣ Display statistics
   - 6️⃣ Exit

## 💡 Input Guidelines

- Titles and genres are automatically capitalized
- Author names are automatically title-cased (e.g., "John Smith")
- Year must be entered as a number
- Reading status must be entered as 'y' or 'n'

## 🛠️ Technical Requirements

- Python 3.x
- UTF-8 terminal support for emoji display

## 📝 Note

The program stores data in 'library.txt' file:
- Books are automatically loaded when starting the program
- Changes are saved after adding/removing books
- Data persists between program sessions
- The library file is stored in the same directory as the program

