from django.test import TestCase

from library.models import Book
from django.db import connection
# Create your tests here.


# Creating main kind of file

books = Book.objects.all()

print(len(connection.queries)) # will result 0 queries as not executed until we use print or something

print(books) # After this connection will show 1 query in connection.queries
print(len(connection.queries))

for book in books:
    print(book.authors.name)

print(len(connection.queries)) #this will result in 7 output , one from above and 6 these queries (N+1). 5 record

# To reduce this case into single query , as it is 1:M relation between table will use select_related

books = Book.objects.select_related('authors')
for book in books:
    print(book.authors.name)

print(len(connection.queries)) # perform the join and return only 1 query









