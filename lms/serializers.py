from rest_framework import serializers
from lms.models import Book,Transaction

class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['img', 'desc']

class Transactionserializer(serializers.ModelSerializer):
    book_title = serializers.ReadOnlyField(source='book.title')
    book_author = serializers.ReadOnlyField(source='book.author.name')
    accession_number= serializers.ReadOnlyField(source='book.accession_number')

    class Meta:
        model = Transaction
        fields = ['accession_number','book_title', 'book_author']
             
