from django.urls import path

from library import views

urlpatterns = \
    [
        path('createbook/', views.create_book, name='createbook'),
        path('createauthor/', views.create_author, name='createauthor'),
        path('get_book/<int:id>', views.get_books, name='get_books'),
        path('get_author/<int:id>', views.get_authors, name='get_authors'),
    ]
