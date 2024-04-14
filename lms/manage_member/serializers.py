from rest_framework import serializers
from lms.models import Student,Staff,Visitor

class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

    def validate_library_id(self, value):
        if value <= 0:
            raise serializers.ValidationError("Library ID must be a positive integer.")
        return value

    def validate_number_card(self, value):
        string="[A-"
        if value.isdigit():
           n=65+int(value)
           s=chr(n)       
           return value +string+s+']'
        else:
           return value
        

    def validate_membership_type(self, value):
        choices = [choice for choice in Staff.member_choices]
        if value not in choices:
            raise serializers.ValidationError("Invalid membership type.")
        return value

    def validate_Department(self, value):       
        choices = [choice for choice in Staff.dep_choices]
        if value not in choices:
            raise serializers.ValidationError("Invalid department.")
        return value
    
class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = '__all__'    

          

