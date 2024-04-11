from rest_framework import serializers
from lms.models import Book
from datetime import datetime

class Create_SeriesBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['book_barcode_image', 'book_image', 'desc']

    def validate_published_year(self, value):
        current_year = datetime.now().year
        if value < 1000 or value > current_year:
            raise serializers.ValidationError("Invalid published year.")
        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative.")
        return value

    def validate_status(self, value):
        valid_statuses = ['Available', 'UnAvailable']
        if value not in valid_statuses:
            raise serializers.ValidationError("Invalid status.")
        return value

    def validate_isbn(self, value):
        if Book.objects.filter(isbn=value).exists():
            raise serializers.ValidationError("ISBN must be unique.")
        return value


class BookSummary_UodateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields=['accession_number','author','book_type','status','book_image', 'desc']

class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields=['accession_number','author','title','book_image']        
