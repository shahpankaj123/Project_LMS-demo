from django.shortcuts import render
from lms.models import Book,Staff,Transaction,Student

from django.db import connection
from datetime import date

from lms.dasboard.serializers import Transactionserializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

# Dashboard Api

class TranscitionPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10

class CountBook_View(APIView):
    def get(self, request, format=None):
        data={}
        try:
            total_books = Book.objects.filter(school_id=2).count()
            data['total_books'] = total_books          
            print(connection.queries)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  

        return Response(data,status=status.HTTP_200_OK)


class CountStudent_View(APIView):
    def get(self, request, format=None):
        data={}
        try:
            total_student=Student.objects.filter(school_id=2).count()
            data['total_students'] = total_student
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
    
        return Response(data,status=status.HTTP_200_OK)
    
class CountStaff_View(APIView):
    def get(self, request, format=None):
        data={}
        try:
            total_staff=Staff.objects.filter(school_id=2).count()
            data['total_staff'] = total_staff
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
    
        return Response(data,status=status.HTTP_200_OK)    
    
class Count_IssuedBook_View(APIView):
    def get(self, request, format=None):
        data={}
        try:
            total_issued=Transaction.objects.filter(school_id=2,return_status='N').count() 
            data['total_issued'] = total_issued
            print(connection.queries)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
    
        return Response(data,status=status.HTTP_200_OK)   

class Count_ToadyIssuedBook_View(APIView):
    def get(self, request, format=None):
        data={}
        today_date = date.today()
        try:
            total_return=Transaction.objects.filter(school_id=2,return_status='N',issue_date=today_date).count() 
            print(connection.queries)
            data['today_issuedbook'] = total_return
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
    
        return Response(data,status=status.HTTP_200_OK)       
    
class Count_ToadyReturnBook_View(APIView):
    def get(self, request, format=None):
        data={}
        today_date = date.today()
        try:
            total_return=Transaction.objects.filter(school_id=2,return_status='Y',return_date=today_date).count() 
            print(connection.queries)
            data['today_Returnbook'] = total_return
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
    
        return Response(data,status=status.HTTP_200_OK)     
           

class List_IssuedBook_View(generics.ListCreateAPIView):
    queryset =Transaction.objects.filter(school_id=2,return_status='N').select_related('book').order_by('-issue_date').only('book__title','book__accession_number','book__author')
    serializer_class =Transactionserializer
    pagination_class =TranscitionPagination

class List_ReturnBook_View(generics.ListCreateAPIView):
    queryset =Transaction.objects.filter(school_id=2,return_status='Y').select_related('book').order_by('-issue_date').only('book__title','book__accession_number','book__author')
    serializer_class =Transactionserializer
    pagination_class =TranscitionPagination
  
