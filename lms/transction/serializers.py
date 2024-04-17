from rest_framework import serializers
from lms.models import Transaction,Book,Student,Staff,Visitor

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['StudentID', 'Photo', 'DOB', 'BirthPlace', 'IdentificationMark', 'AdhaarNo', 'PassportNo',
                  'MedicalCondition', 'PermanentAddressLine1', 'PermanentAddressLine2', 'TemporaryAddressLine1',
                  'TemporaryAddressLine2', 'IsActive', 'PanCardNo', 'VoterID', 'PreviousSchoolName',
                  'PrevSchoolDiseCode', 'TransferCertificateNo', 'SATSNo', 'SchoolID', 'CreatedAt', 'UpdatedAt',
                  'AdmissionNo', 'AdmissionDate']

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

     