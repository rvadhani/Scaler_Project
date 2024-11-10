from logging import exception

from django.db.models import Q
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from library.models import Book, Author
from library.serializer import BookSerializer, AuthorSerializer


# Create your views here.

@api_view(['POST'])
def create_book(request):
    book_serializer = BookSerializer(data=request.data)

    if book_serializer.is_valid():
        book_serializer.save()

        return Response(book_serializer.data, status=status.HTTP_201_CREATED)

    return Response(book_serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_author(request):
    author_serializer = AuthorSerializer(data=request.data)

    if author_serializer.is_valid():
        author_serializer.save()
        return Response(author_serializer.data, status = status.HTTP_201_CREATED)

    return Response(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_books(request,id):
    # Queryset Q to be use for AND, OR ,LIKE, IN  operators
    book = Book.objects.filter(~(Q(title__icontains="rowling")) | Q(pk=id))
    print(book[0].__dict__)
    print(BookSerializer(book, many=True).data)
    try:
        book_serializer = BookSerializer(Book.objects.get(pk=id))
        return Response(book_serializer.data, status=status.HTTP_200_OK)
    except Book.DoesNotExist:
        return Response('NOT_FOUND', status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_authors(request,id):
    try:
        author_serializer = AuthorSerializer(Author.objects.get(pk=id))
        return Response(author_serializer.data, status=status.HTTP_200_OK)
    except Author.DoesNotExist:
        return Response('NOT_FOUND', status=status.HTTP_404_NOT_FOUND)
