from rest_framework import serializers
from lms.models import Transaction,Book,Student,Staff,Visitor

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['StudentID', 'Photo', 'DOB', 'SchoolID', 
                  'AdmissionNo']

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['library_id', 'name', 'number_card', 'membership_type', 'Department','phone']

class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = ['name', 'phone', 'Referred_by', 'membership_type', 'visit_type', 'address', 'status']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['accession_number', 'author', 'title']

class TransactionSerializer(serializers.ModelSerializer):
    borrower = serializers.SerializerMethodField()
    class Meta:
        model = Transaction
        fields = ['borrower']

    def get_borrower(self, obj):
        if obj.student:
            return StudentSerializer(obj.student).data
        elif obj.staff:
            return StaffSerializer(obj.staff).data
        elif obj.visitor:
            return VisitorSerializer(obj.visitor).data
        else:
            return None

class TransactionSerializer1(serializers.ModelSerializer):
    book = BookSerializer()
    class Meta:
        model = Transaction
        fields = ['book', 'issue_date', 'due_date', 'return_status']

class BookListSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields=['accession_number','author_name','title','book_image']   

    def get_author_name(self, obj):
        return obj.author.name if obj.author else None      
    
class BookSerializer1(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)
    publisher_name = serializers.CharField(source='publisher.name', read_only=True)
    book_type_name = serializers.CharField(source='book_type.name', read_only=True)

    class Meta:
        model = Book
        fields = ['accession_number', 'author_name', 'publisher_name', 'published_year', 'book_type_name']

class ReturnbookSerializer(serializers.ModelSerializer):
    borrower = serializers.SerializerMethodField()
    book = BookSerializer1()
    class Meta:
        model = Transaction
        fields = ['borrower','book', 'issue_date', 'due_date', 'return_status']

    def get_borrower(self, obj):
        if obj.student:
            return StudentSerializer(obj.student).data
        elif obj.staff:
            return StaffSerializer(obj.staff).data
        elif obj.visitor:
            return VisitorSerializer(obj.visitor).data
        else:
            return None    