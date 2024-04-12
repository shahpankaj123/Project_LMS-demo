from rest_framework import serializers
from lms.models import Student,Staff

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

    def validate_name(self, value):
        return value

    def validate_number_card(self, value):
        # Add custom validation for the number_card field if needed
        return value

    def validate_membership_type(self, value):
        # Check if membership_type is one of the choices
        choices = [choice[0] for choice in Staff.member_choices]
        if value not in choices:
            raise serializers.ValidationError("Invalid membership type.")
        return value

    def validate_Department(self, value):
        # Check if Department is one of the choices
        choices = [choice[0] for choice in Staff.dep_choices]
        if value not in choices:
            raise serializers.ValidationError("Invalid department.")
        return value

    def validate_email(self, value):
        # Add custom validation for the email field if needed
        return value

    def validate_phone(self, value):
        # Add custom validation for the phone field if needed
        return value
          

