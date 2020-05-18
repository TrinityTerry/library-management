from ...models import Book

def update_book(form_data, book_id):
    book = Book.objects.get(pk=book_id)
    book.title= form_data['title']
    book.author= form_data['author'] 
    book.isbn= form_data['isbn']
    book.year_published= form_data['year_published']
    book.location_id= form_data['location']
    book.save()

