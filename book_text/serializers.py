from rest_framework import serializers, filters
from rest_framework.serializers import ModelSerializer
from django_filters import rest_framework as filters
from book_text.models import Book, Type, Author, AuthorType


class BookSerializers(ModelSerializer):
    author = serializers.SerializerMethodField()
    add_time= serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    type = serializers.CharField(source='type.name',read_only=True)
    def get_author(self, obj):
        value_list =  AuthorType.objects.filter(book=obj.id).values("author__name",'author_id')
        return value_list
    class Meta:
        model = Book
        fields = "__all__"
        # depth=1


class TypeSerializers(ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"
        # depth=1

class AuthorSerializers(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
        # depth=1


class BookFilter(filters.FilterSet):
    class Meta:
        # min_read = filters.NumberFilter(field_name="bread", lookup_expr='gte')
        # max_read = filters.NumberFilter(field_name="bread", lookup_expr='lte')
        model = Book  # 模型名
        fields = {
            'name':['icontains'],
            # 'bcomment':['gte','lte'],
        }