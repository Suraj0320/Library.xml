import tkinter as tk
from tkinter import messagebox
import xml.etree.ElementTree as ET

# Create a Tkinter window
window = tk.Tk()
window.title("Library Interface")

# Function for searching books
# Function for searching books
def search_books():
    search_query = entry_search.get()
    # Read the XML file
    tree = ET.parse("library.xml")
    root = tree.getroot()
    
    found_books = []
    
    # Search for books matching the query
    for book in root.findall(".//book"):
        title = book.find("title").text
        author = book.find("author").text
        publisher = book.find("publisher").text
        publication_date = book.find("publication_date").text
        isbn = book.find("isbn").text
        genre = book.find("genre").text
        copies_available = book.find("copies_available").text
        
        if search_query.lower() in title.lower():
            found_books.append(f"Title: {title}\nAuthor: {author}\nPublisher: {publisher}\nPublication Date: {publication_date}\nISBN: {isbn}\nGenre: {genre}\nCopies Available: {copies_available}\n")
    
    # Display search results
    if found_books:
        messagebox.showinfo("Search Results", "\n\n".join(found_books))
    else:
        messagebox.showinfo("Search Results", "No books found.")

# Create labels and entry fields
label_search = tk.Label(window, text="Search Books:")
entry_search = tk.Entry(window)
button_search = tk.Button(window, text="Search", command=search_books)

# Arrange the widgets using grid layout
label_search.grid(row=0, column=0)
entry_search.grid(row=0, column=1)
button_search.grid(row=0, column=2)

# Function for adding books
def add_book():
    title = entry_title.get()
    author = entry_author.get()
    publisher = entry_publisher.get()
    publication_date = entry_publication_date.get()
    isbn = entry_isbn.get()
    genre = entry_genre.get()
    copies_available = entry_copies_available.get()
    
    # Create a new book element
    new_book = ET.Element("book")
    ET.SubElement(new_book, "title").text = title
    ET.SubElement(new_book, "author").text = author
    ET.SubElement(new_book, "publisher").text = publisher
    ET.SubElement(new_book, "publication_date").text = publication_date
    ET.SubElement(new_book, "isbn").text = isbn
    ET.SubElement(new_book, "genre").text = genre
    ET.SubElement(new_book, "copies_available").text = copies_available
    
    # Append the new book element to the XML file
    tree = ET.parse("library.xml")
    root = tree.getroot()
    books = root.find("books")
    books.append(new_book)
    tree.write("library.xml")
    
    messagebox.showinfo("Book Added", f"Book added to the library: {title} by {author}")

# Create labels and entry fields
label_search = tk.Label(window, text="Search Books:")
entry_search = tk.Entry(window)
button_search = tk.Button(window, text="Search", command=search_books)

label_title = tk.Label(window, text="Title:")
entry_title = tk.Entry(window)
label_author = tk.Label(window, text="Author:")
entry_author = tk.Entry(window)
label_publisher = tk.Label(window, text="Publisher:")
entry_publisher = tk.Entry(window)
label_publication_date = tk.Label(window, text="Publication Date:")
entry_publication_date = tk.Entry(window)
label_isbn = tk.Label(window, text="ISBN:")
entry_isbn = tk.Entry(window)
label_genre = tk.Label(window, text="Genre:")
entry_genre = tk.Entry(window)
label_copies_available = tk.Label(window, text="Copies Available:")
entry_copies_available = tk.Entry(window)
button_add = tk.Button(window, text="Add Book", command=add_book)

# Arrange the widgets using grid layout
label_search.grid(row=0, column=0)
entry_search.grid(row=0, column=1)
button_search.grid(row=0, column=2)

label_title.grid(row=1, column=0)
entry_title.grid(row=1, column=1)
label_author.grid(row=2, column=0)
entry_author.grid(row=2, column=1)
label_publisher.grid(row=3, column=0)
entry_publisher.grid(row=3, column=1)
label_publication_date.grid(row=4, column=0)
entry_publication_date.grid(row=4, column=1)
label_isbn.grid(row=5, column=0)
entry_isbn.grid(row=5, column=1)
label_genre.grid(row=6, column=0)
entry_genre.grid(row=6, column=1)
label_copies_available.grid(row=7, column=0)
entry_copies_available.grid(row=7, column=1)
button_add.grid(row=8, column=1)

# Start the Tkinter event loop
window.mainloop()

