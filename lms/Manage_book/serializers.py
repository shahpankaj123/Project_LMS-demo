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


class BookSummary_UodateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields=['accession_number','author','book_type','status','book_image', 'desc']

class BookListSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields=['accession_number','author_name','title','book_image']   

    def get_author_name(self, obj):
        return obj.author.name if obj.author else None         


class BookImg_ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields=['accession_number','author','book_type','status','book_image', 'book_image']


class BookImg_UpdateSerializer(serializers.ModelSerializer):

    def validate_book_image(self, value):
        if not value.content_type.startswith('image'):
            raise serializers.ValidationError("Only image files are allowed.")
        
        max_size = 10 * 1024 * 1024  # 10MB
        if value.size > max_size:
            raise serializers.ValidationError("File size too large. Max size is 10 MB.")

        return value   

    class Meta:
        model = Book
        fields=['accession_number','book_image'] 
