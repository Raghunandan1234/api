from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Dummy data to simulate a database
class Book(BaseModel):
    id: int
    title: str
    author: str

books = [
    Book(id=1, title="Book 1", author="Author 1"),
    Book(id=2, title="Book 2", author="Author 2"),
    Book(id=3, title="Book 3", author="Author 3"),
]

# Route to get all books
@app.get("/api/books", response_model=list[Book])
def get_books():
    return books

# Route to get a specific book by its ID
@app.get("/api/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = next((item for item in books if item.id == book_id), None)
    if book:
        return book
    else:
        raise HTTPException(status_code=404, detail="Book not found")

# Route to add a new book
@app.post("/api/books", response_model=Book)
def add_book(book: Book):
    books.append(book)
    return book

# Route to update an existing book
@app.put("/api/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    book = next((item for item in books if item.id == book_id), None)
    if book:
        book.title = updated_book.title
        book.author = updated_book.author
        return book
    else:
        raise HTTPException(status_code=404, detail="Book not found")

# Route to delete a book by its ID
@app.delete("/api/books/{book_id}", response_model=Book)
def delete_book(book_id: int):
    global books
    book = next((item for item in books if item.id == book_id), None)
    if book:
        books = [item for item in books if item.id != book_id]
        return book
    else:
        raise HTTPException(status_code=404, detail="Book not found")


