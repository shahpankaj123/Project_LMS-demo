from rest_framework import serializers
from lms.models import Book,Location,Transaction

class BookReportSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields = ['accession_number','title','author']

class LocationReportSerializer(serializers.ModelSerializer):
    class Meta:
        model=Location
        fields='__all__'     


class TransctionReportSerializer(serializers.ModelSerializer):
    book_info = BookReportSerializer(source='book', read_only=True)
    class Meta:
        model=Transaction
        fields = ['borrower_id','book_info','issue_date','due_date']        