from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from book_text.models import Book, Type, Author, AuthorType
from book_text.serializers import BookSerializers, TypeSerializers, AuthorSerializers, BookFilter
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters.SearchFilter

class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    filter_fields = {'name': ['exact','contains'], 'release_time': ['year', 'month', 'day', 'gte', 'lte'], "price": ['exact', 'gte', 'lte']}

    def create(self, request, *args, **kwargs):
        value = request.data
        bookValue = value.pop("author")
        value['type'] = Type.objects.filter(id=value['type']).first()
        createObj = Book.objects.create(**value)
        createList = []
        for i in bookValue:
            authorObj = Author.objects.filter(id=i).first()
            createList.append(AuthorType(book=createObj, author=authorObj))
        AuthorType.objects.bulk_create(createList)
        return Response("成功")

    def perform_create(self, serializer):
        serializer.save()

# all { name: string, price: int, type: int, author: array }
# Create { name: string, price: int, type: int, }
# 获取创建好的book_id: array
# booid  和author 创建
# 进行关联表的数据
# 关联表 { }


class TypeModelViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializers

class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers