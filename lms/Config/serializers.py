from rest_framework import serializers
from lms.models import Author,Publisher,Supplier,Subject,Language,Editor,Book_Type,Remark,Location,Book


class BarcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['accession_number', 'book_barcode_image']



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Author cannot be empty")
        if len(value) < 5:
            raise serializers.ValidationError("Author must have alteast 5 characters")
        if  value.isalnum():
            raise serializers.ValidationError("Author must not consist  of alphanumeric characters")
        return value
    
class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Publisher cannot be empty")
        if len(value) < 5:
            raise serializers.ValidationError("Publisher must have alteast 5 characters")
        if  value.isalnum():
            raise serializers.ValidationError("Publisher must not consist  of alphanumeric characters")
        return value

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Supplier cannot be empty")
        if len(value) < 5:
            raise serializers.ValidationError("Supplier must have alteast 5 characters")
        if  value.isalnum():
            raise serializers.ValidationError("Supplier must not consist  of alphanumeric characters")
        return value

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Subject cannot be empty")
        if len(value) < 3:
            raise serializers.ValidationError("Subject must have alteast 3 characters")
        if  value.isalnum():
            raise serializers.ValidationError("Subject must not consist  of alphanumeric characters")
        return value

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['name']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Language cannot be empty")
        if len(value) < 3:
            raise serializers.ValidationError("Language must have alteast 3 characters")
        if  value.isalnum():
            raise serializers.ValidationError("Language must not consist  of alphanumeric characters")
        return value

class EditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editor
        fields = ['name']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Editor cannot be empty")
        if len(value) < 5:
            raise serializers.ValidationError("Editor must have alteast 5 characters")
        if  value.isalnum():
            raise serializers.ValidationError("Editor must not consist  of alphanumeric characters")
        return value

class Book_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_Type
        fields = ['name']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Book_Type cannot be empty")
        if len(value) < 3:
            raise serializers.ValidationError("Book_Type must have alteast 3 characters")
        if  value.isalnum():
            raise serializers.ValidationError("Book_Type must not consist  of alphanumeric characters")
        return value

class RemarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remark
        fields = ['name']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Remark cannot be empty")
        if len(value) < 3:
            raise serializers.ValidationError("Remark must have alteast 3 characters")
        if  value.isalnum():
            raise serializers.ValidationError("Remark must not consist  of alphanumeric characters")
        return value

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Location cannot be empty")
        if len(value) < 2:
            raise serializers.ValidationError("Location must have alteast 2 characters")
        if  value.isalnum():
            raise serializers.ValidationError("Location must not consist  of alphanumeric characters")
        return value    

