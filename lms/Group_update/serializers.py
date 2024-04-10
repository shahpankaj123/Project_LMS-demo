from rest_framework import serializers
from lms. models import Book


class UpdateSubjectSerializer(serializers.ModelSerializer):
    accession_number1 = serializers.CharField(write_only=True)
    accession_number2 = serializers.CharField(write_only=True)

    class Meta:
        model = Book
        fields = ['accession_number1', 'accession_number2', 'subject']

    def validate(self, data):
        accession_number1 = data.get('accession_number1')
        accession_number2 = data.get('accession_number2')

        # Validate accession numbers
        if int(accession_number1) < 1 or int(accession_number1) < 1 :
            raise serializers.ValidationError("Accession number  must be greater than 0")

        if accession_number1 >= accession_number2:
            raise serializers.ValidationError("Accession number 1 must be smaller than accession number 2")
        
        return data


class UpdateLocationSerializer(serializers.ModelSerializer):
    accession_number1 = serializers.CharField(write_only=True)
    accession_number2 = serializers.CharField(write_only=True)

    class Meta:
        model = Book
        fields = ['accession_number1', 'accession_number2', 'location']

    def validate(self, data):
        accession_number1 = data.get('accession_number1')
        accession_number2 = data.get('accession_number2')

        # Validate accession numbers
        if int(accession_number1) < 1 or int(accession_number2) < 1 :
            raise serializers.ValidationError("Accession number  must be greater than 0")

        if accession_number1 >= accession_number2:
            raise serializers.ValidationError("Accession number 1 must be smaller than accession number 2")
        
        return data
    
class UpdateRemarksSerializer(serializers.ModelSerializer):
    accession_number1 = serializers.CharField(write_only=True)
    accession_number2 = serializers.CharField(write_only=True)

    class Meta:
        model = Book
        fields = ['accession_number1', 'accession_number2', 'remarks']

    def validate(self, data):
        accession_number1 = data.get('accession_number1')
        accession_number2 = data.get('accession_number2')

        # Validate accession numbers
        if int(accession_number1) < 1 or int(accession_number2) < 1 :
            raise serializers.ValidationError("Accession number  must be greater than 0")

        if accession_number1 >= accession_number2:
            raise serializers.ValidationError("Accession number 1 must be smaller than accession number 2")
        
        return data  

class UpdateSupplierSerializer(serializers.ModelSerializer):
    accession_number1 = serializers.CharField(write_only=True)
    accession_number2 = serializers.CharField(write_only=True)

    class Meta:
        model = Book
        fields = ['accession_number1', 'accession_number2', 'supplier']

    def validate(self, data):
        accession_number1 = data.get('accession_number1')
        accession_number2 = data.get('accession_number2')

        # Validate accession numbers
        if int(accession_number1) < 1 or int(accession_number2) < 1 :
            raise serializers.ValidationError("Accession number  must be greater than 0")

        if accession_number1 >= accession_number2:
            raise serializers.ValidationError("Accession number 1 must be smaller than accession number 2")
        
        return data  

class UpdatePublisherSerializer(serializers.ModelSerializer):
    accession_number1 = serializers.CharField(write_only=True)
    accession_number2 = serializers.CharField(write_only=True)

    class Meta:
        model = Book
        fields = ['accession_number1', 'accession_number2', 'publisher']

    def validate(self, data):
        accession_number1 = data.get('accession_number1')
        accession_number2 = data.get('accession_number2')

        # Validate accession numbers
        if int(accession_number1) < 1 or int(accession_number2) < 1 :
            raise serializers.ValidationError("Accession number  must be greater than 0")

        if accession_number1 >= accession_number2:
            raise serializers.ValidationError("Accession number 1 must be smaller than accession number 2")
        
        return data     


class UpdateBookTypeSerializer(serializers.ModelSerializer):
    accession_number1 = serializers.CharField(write_only=True)
    accession_number2 = serializers.CharField(write_only=True)

    class Meta:
        model = Book
        fields = ['accession_number1', 'accession_number2', 'book_type']

    def validate(self, data):
        accession_number1 = data.get('accession_number1')
        accession_number2 = data.get('accession_number2')

        # Validate accession numbers
        if int(accession_number1) < 1 or int(accession_number2) < 1 :
            raise serializers.ValidationError("Accession number  must be greater than 0")

        if accession_number1 >= accession_number2:
            raise serializers.ValidationError("Accession number 1 must be smaller than accession number 2")
        
        return data       

class UpdateBookStatusSerializer(serializers.ModelSerializer):
    accession_number1 = serializers.CharField(write_only=True)
    accession_number2 = serializers.CharField(write_only=True)

    class Meta:
        model = Book
        fields = ['accession_number1', 'accession_number2', 'status']

    def validate(self, data):
        accession_number1 = data.get('accession_number1')
        accession_number2 = data.get('accession_number2')

        # Validate accession numbers
        if int(accession_number1) < 1 or int(accession_number2) < 1 :
            raise serializers.ValidationError("Accession number  must be greater than 0")

        if accession_number1 >= accession_number2:
            raise serializers.ValidationError("Accession number 1 must be smaller than accession number 2")
        
        return data       

class UpdateBillInfoSerializer(serializers.ModelSerializer):
    accession_number1 = serializers.CharField(write_only=True)
    accession_number2 = serializers.CharField(write_only=True)

    class Meta:
        model = Book
        fields = ['accession_number1', 'accession_number2', 'bill_number','bill_date']

    def validate(self, data):
        accession_number1 = data.get('accession_number1')
        accession_number2 = data.get('accession_number2')

        # Validate accession numbers
        if int(accession_number1) < 1 or int(accession_number2) < 1 :
            raise serializers.ValidationError("Accession number  must be greater than 0")

        if accession_number1 >= accession_number2:
            raise serializers.ValidationError("Accession number 1 must be smaller than accession number 2")
        
        return data     

class Update_No_of_page_Serializer(serializers.ModelSerializer):
    accession_number1 = serializers.CharField(write_only=True)
    accession_number2 = serializers.CharField(write_only=True)

    class Meta:
        model = Book
        fields = ['accession_number1', 'accession_number2', 'page_no']

    def validate(self, data):
        accession_number1 = data.get('accession_number1')
        accession_number2 = data.get('accession_number2')

        # Validate accession numbers
        if int(accession_number1) < 1 or int(accession_number2) < 1 :
            raise serializers.ValidationError("Accession number  must be greater than 0")

        if accession_number1 >= accession_number2:
            raise serializers.ValidationError("Accession number 1 must be smaller than accession number 2")
        
        return data         
    
class Update_BookPublishedYearSerializer(serializers.ModelSerializer):
    accession_number1 = serializers.CharField(write_only=True)
    accession_number2 = serializers.CharField(write_only=True)

    class Meta:
        model = Book
        fields = ['accession_number1', 'accession_number2', 'published_year']

    def validate(self, data):
        accession_number1 = data.get('accession_number1')
        accession_number2 = data.get('accession_number2')

        # Validate accession numbers
        if int(accession_number1) < 1 or int(accession_number2) < 1 :
            raise serializers.ValidationError("Accession number  must be greater than 0")

        if accession_number1 >= accession_number2:
            raise serializers.ValidationError("Accession number 1 must be smaller than accession number 2")
        
        return data   

class Update_BookPriceSerializer(serializers.ModelSerializer):
    accession_number1 = serializers.CharField(write_only=True)
    accession_number2 = serializers.CharField(write_only=True)

    class Meta:
        model = Book
        fields = ['accession_number1', 'accession_number2', 'price']

    def validate(self, data):
        accession_number1 = data.get('accession_number1')
        accession_number2 = data.get('accession_number2')

        # Validate accession numbers
        if int(accession_number1) < 1 or int(accession_number2) < 1 :
            raise serializers.ValidationError("Accession number  must be greater than 0")

        if accession_number1 >= accession_number2:
            raise serializers.ValidationError("Accession number 1 must be smaller than accession number 2")
        
        return data          