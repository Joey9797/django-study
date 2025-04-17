from rest_framework import serializers
from .models import Book, Review


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', )


class BookSerializer(serializers.ModelSerializer):

    review_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Book
        fields = ('id', 'reviews', 'review_count', 'isbn', 'author', 'title',)

    class ReviewDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('content', 'score')

    reviews = ReviewDetailSerializer(read_only=True, many=True)


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('book', 'content', 'score',)

    class BookDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Book
            fields = ('isbn',)
    
    book = BookDetailSerializer(read_only=True)


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('book',)