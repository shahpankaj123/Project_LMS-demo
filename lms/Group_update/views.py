from lms.models import Book,Staff,Student,Transaction
from django.db import connection
from datetime import date

from lms.Group_update.serializers import UpdateSubjectSerializer,UpdateLocationSerializer,UpdateRemarksSerializer,UpdateSupplierSerializer,UpdatePublisherSerializer,UpdateBookTypeSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


class UpdateSubjectView(APIView):
    def put(self, request):
        serializer = UpdateSubjectSerializer(data=request.data)
        if serializer.is_valid():
            accession_number1 = serializer.validated_data['accession_number1']
            accession_number2 = serializer.validated_data['accession_number2']
            subject = serializer.validated_data['subject']

            # Update subjects for books within the specified accession number range
            books_to_update = Book.objects.filter(accession_number__gte=accession_number1,
                                                   accession_number__lte=accession_number2)
            books_to_update.update(subject=subject)
            print(connection.queries)

            return Response({"Info":"Subject Updates Successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UpdateLocationView(APIView):

    def put(self, request):
        serializer = UpdateLocationSerializer(data=request.data)
        if serializer.is_valid():
            accession_number1 = serializer.validated_data['accession_number1']
            accession_number2 = serializer.validated_data['accession_number2']
            location = serializer.validated_data['location']

            books_to_update = Book.objects.filter(accession_number__gte=accession_number1,
                                                   accession_number__lte=accession_number2)
            books_to_update.update(location=location)
            print(connection.queries)

            return Response({"Info":"Location Updates Successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
class UpdateRemarksView(APIView):

    def put(self, request):
        serializer = UpdateRemarksSerializer(data=request.data)
        if serializer.is_valid():
            accession_number1 = serializer.validated_data['accession_number1']
            accession_number2 = serializer.validated_data['accession_number2']
            remarks = serializer.validated_data['remarks']

            books_to_update = Book.objects.filter(accession_number__gte=accession_number1,
                                                   accession_number__lte=accession_number2)
            books_to_update.update(remarks=remarks)
            print(connection.queries)

            return Response({"Info":"Remarks Updates Successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      
    

class UpdateSupplierView(APIView):

    def put(self, request):
        serializer =UpdateSupplierSerializer(data=request.data)
        if serializer.is_valid():
            accession_number1 = serializer.validated_data['accession_number1']
            accession_number2 = serializer.validated_data['accession_number2']
            supplier= serializer.validated_data['supplier']

            books_to_update = Book.objects.filter(accession_number__gte=accession_number1,
                                                   accession_number__lte=accession_number2)
            books_to_update.update(supplier=supplier)
            print(connection.queries)

            return Response({"Info":"Supplier Updates Successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
class UpdatePublisherView(APIView):

    def put(self, request):
        serializer =UpdatePublisherSerializer(data=request.data)
        if serializer.is_valid():
            accession_number1 = serializer.validated_data['accession_number1']
            accession_number2 = serializer.validated_data['accession_number2']
            publisher= serializer.validated_data['publisher']

            books_to_update = Book.objects.filter(accession_number__gte=accession_number1,
                                                   accession_number__lte=accession_number2)
            books_to_update.update(publisher=publisher)
            print(connection.queries)

            return Response({"Info":"Publisher Updates Successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       
    
class UpdateBookTypeView(APIView):

    def put(self, request):
        serializer =UpdateBookTypeSerializer(data=request.data)
        if serializer.is_valid():
            accession_number1 = serializer.validated_data['accession_number1']
            accession_number2 = serializer.validated_data['accession_number2']           
            book_type= serializer.validated_data['book_type']           

            books_to_update = Book.objects.filter(accession_number__gte=accession_number1,
                                                   accession_number__lte=accession_number2)
            books_to_update.update(book_type=book_type)
            print(connection.queries)

            return Response({"Info":"BookType Updates Successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     