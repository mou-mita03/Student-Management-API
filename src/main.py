from fastapi import FastAPI,HTTPException #এটা FastAPI framework নিয়ে আসে।FastAPI দিয়ে আমরা API route বানাই।
from pydantic import BaseModel #এটা data structure বানানোর জন্য।


app = FastAPI(title="BookShop API") #এখানে আমরা FastAPI application বানাচ্ছি।app হলো আমাদের main object like a variable।



class Book(BaseModel): #এখানে আমরা একটা Book class বানাচ্ছি।এটা database না।এটা হলো data format।
    id: int
    title: str
    author: str
    price: float
    quantity: int


books = [   #এটা আমাদের temporary database।এখন আমরা real database ব্যবহার করছি না।RAM এর ভিতরে data রাখছি।
    Book(
        id=1,
        title="Python Crash Course", 
        author="Eric Matthes", 
        price=2500, 
        quantity=10
        ),
    Book(
        id=2,
        title="Clean Code",
        author="Robert C. Martin",
        price=3000,
        quantity=5
        )
    ]


 #Get - Get all books
@app.get("/books") #যদি কেউ browser এ যায়:GET localhost:8000/books|তাহলে এই function চলবে।
def get_books():  #এটা execute হবে।
    return books  #মানে সব বই পাঠিয়ে দাও।


#Get - Get a book by ID
@app.get("/books/{book_id}")  #{book_id} = dynamic value।
def get_book(book_id: int):   #মানে id integer হবে।
    for book in books:        #এক এক করে সব বই দেখবে।
        if book.id == book_id:
            return book
        
    raise HTTPException(
        status_code=404, 
        detail="Book not found"
    )

#Post - Add a new book
@app.post("/books", status_code=201)  #POST মানে নতুন data পাঠানো।201 = Created
def create_book(book: Book):          #মানে incoming data অবশ্যই Book format হতে হবে।book হচ্ছে একটা variable যা এই funtion এর parameter একটা।

    for existing_book in books:       #Duplicate check:সব বই check করবে।
        if existing_book.id == book.id:
            raise HTTPException(
                status_code=400, #400 = Bad Request
                detail="Book ID already exists"
            )
        
    books.append(book)  #append() নতুন বই list এ যোগ করে।

    return book


#Put - Update a book
@app.put("/books/{book_id}")  #PUT মানে update।
def update_book(book_id: int, updated_book: Book): 
    for index, book in enumerate(books): #index = position|enumerate() ব্যবহার করে আমরা একসাথে index (position) এবং value (item) পাই।enumerate() list-এর প্রতিটা item-এর সাথে তার index যোগ করে দেয়।
        if book.id == book_id:  
            books[index] = updated_book  #যদি id মিলে:পুরানো বই replace হবে।
            return updated_book
        
    raise HTTPException(
        status_code=404, #404 = Not Found
        detail="Book not found"
    )                     


#Delete - Delete a book
@app.delete("/books/{book_id}") #মানে delete request।
def delete_book(book_id: int): 
    for index, book in enumerate(books):   #খুঁজবে।
        if book.id == book_id:
            deleted_book = books.pop(index) #pop() list থেকে remove করে।
            return {
                "message": "Book deleted successfully",
                "book": deleted_book
            }   
        
    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )