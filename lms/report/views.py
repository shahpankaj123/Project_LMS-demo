from lms.report.serializers import LocationReportSerializer,BookReportSerializer,TransctionReportSerializer
from lms.models import Location,Book,Transaction
from django.db import connection
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics


class LocationReport_View(APIView):
    def get(self, request, format=None):
        Loc_obj = Location.objects.all()
        serializer = LocationReportSerializer(Loc_obj, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request, format=None):   
        Location_id = request.data.get('Location_id')

        if Location_id  is None:
            return Response({"error": "Location_id  not found in request data."}, status=status.HTTP_400_BAD_REQUEST)
        
        if not Location_id.isdigit():
           return Response({"error": "Location_id must be an integer."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
           books = Book.objects.filter(location=Location_id)
        except ObjectDoesNotExist:
            return Response({"error": "data  not found in request data"}, status=status.HTTP_400_BAD_REQUEST)


        book_serializer = BookReportSerializer(books,many=True)
        return Response({'info':'Success','data':book_serializer.data}, status=status.HTTP_200_OK)
    
class IssuedBookReport_View(APIView):   
    def post(self, request, format=None):   
        from_date = request.data.get('from_date')
        to_date = request.data.get('to_date')

        if from_date and to_date is None:
            return Response({"error": "data  not found in request data."}, status=status.HTTP_400_BAD_REQUEST)
        
    
        try:
            date1 = datetime.strptime(from_date, '%Y-%m-%d').date()
            date2 = datetime.strptime(to_date, '%Y-%m-%d').date()
        except ValueError:
            return Response({"error": "Invalid date format. Date must be in YYYY-MM-DD format."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            books = Transaction.objects.filter(issue_date__gte=date1, issue_date__lte=date2).select_related('book')
        except ObjectDoesNotExist:
            return Response({"error": "data  not found in request data"}, status=status.HTTP_400_BAD_REQUEST)
        

        book_serializer = TransctionReportSerializer(books,many=True)
        return Response({'info':'Success','data':book_serializer.data}, status=status.HTTP_200_OK)   
        
    
class ReturnBookReport_View(APIView):   

    def post(self, request, format=None):   
        from_date = request.data.get('from_date')
        to_date = request.data.get('to_date')

        if from_date and to_date is None:
            return Response({"error": "data  not found in request data."}, status=status.HTTP_400_BAD_REQUEST)
        
    
        try:
            date1 = datetime.strptime(from_date, '%Y-%m-%d').date()
            date2 = datetime.strptime(to_date, '%Y-%m-%d').date()
        except ValueError:
            return Response({"error": "Invalid date format. Date must be in YYYY-MM-DD format."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            books = Transaction.objects.filter(due_date__gte=date1,due_date__lte=date2,return_status='Y').select_related('book')
        except ObjectDoesNotExist:
            return Response({"error": "data  not found in request data"}, status=status.HTTP_400_BAD_REQUEST)
        

        book_serializer = TransctionReportSerializer(books,many=True)
        return Response({'info':'Success','data':book_serializer.data}, status=status.HTTP_200_OK) 

class DueBookReport_View(APIView):   

    def post(self, request, format=None):   
        from_date = request.data.get('from_date')
        to_date = request.data.get('to_date')

        if from_date and to_date is None:
            return Response({"error": "data  not found in request data."}, status=status.HTTP_400_BAD_REQUEST)
        
    
        try:
            date1 = datetime.strptime(from_date, '%Y-%m-%d').date()
            date2 = datetime.strptime(to_date, '%Y-%m-%d').date()
        except ValueError:
            return Response({"error": "Invalid date format. Date must be in YYYY-MM-DD format."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            books = Transaction.objects.filter(due_date__gte=date1,due_date__lte=date2,return_status='N').select_related('book')
        except ObjectDoesNotExist:
            return Response({"error": "data  not found in request data"}, status=status.HTTP_400_BAD_REQUEST)
        

        book_serializer = TransctionReportSerializer(books,many=True)
        return Response({'info':'Success','data':book_serializer.data}, status=status.HTTP_200_OK)  

class DueAllBookReport_View(APIView):   
  def get(self, request, format=None):       
    try:
        books = Transaction.objects.filter(return_status='N').select_related('book')
    except ObjectDoesNotExist:
        return Response({"error": "data  not found in request data"}, status=status.HTTP_400_BAD_REQUEST) 

    book_serializer = TransctionReportSerializer(books,many=True)
    return Response({'info':'Success','data':book_serializer.data}, status=status.HTTP_200_OK)            


     
