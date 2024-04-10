from rest_framework import serializers
from lms.models import Transaction

class Transactionserializer(serializers.ModelSerializer):
    book_title = serializers.ReadOnlyField(source='book.title')
    book_author = serializers.ReadOnlyField(source='book.author.name')
    accession_number= serializers.ReadOnlyField(source='book.accession_number')

    class Meta:
        model = Transaction
        fields = ['accession_number','book_title', 'book_author']
             
