from rest_framework import serializers
from lms.models import FineSetting,Book_Type

class FineSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model=FineSetting
        fields='__all__'

class BookTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book_Type
        fields='__all__'
