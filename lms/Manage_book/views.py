from lms.Manage_book.serializers import Create_SeriesBookSerializer,BookSummary_UodateSerializer,BookListSerializer
from lms.models import Book
from django.db import connection
from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status


class Create_SeriesBookView(APIView):

    def get(self, request, format=None):
        data={}
        try:
            book = Book.objects.latest('accession_number').accession_number
            data['old_accn_no']=book
            data['new_accn_no']=book+1
        except Book.DoesNotExist:
            raise Http404("No books found.")
        return Response(data,status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        serializer = Create_SeriesBookSerializer(data=request.data)       
        if serializer.is_valid():
            serializer.save()
            return Response({'info':'Success','data':serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     
class Create_CustomBookView(APIView):

    def post(self, request, format=None):
        serializer = Create_SeriesBookSerializer(data=request.data)       
        if serializer.is_valid():
            serializer.save()
            return Response({'info':'Success','data':serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class BookSummary_UodateView(APIView):
    def post(self, request, format=None):
        accession_number = request.data.get('accession_number')
        if accession_number is None:
            return Response({"error": "accession_number not found in request data."}, status=status.HTTP_400_BAD_REQUEST)

        book = get_object_or_404(Book, accession_number=accession_number)

        book_serializer = BookSummary_UodateSerializer(book)
        return Response({'info':'Success','data':book_serializer.data}, status=status.HTTP_200_OK)
    
    def put(self, request, format=None):
        book_id = request.data.get('accession_number')
        new_desc = request.data.get('desc')

        if not book_id or not new_desc:
            return Response({"error": "Book ID and new description are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        book = get_object_or_404(Book, accession_number=book_id)
        book.desc = new_desc
        book.save()
        book_serializer = BookSummary_UodateSerializer(book)
        return Response({'info':'Success','data':book_serializer.data}, status=status.HTTP_200_OK)
    
class BookList_View(APIView):
    queryset = Book.objects.all()
    serializer_class =BookListSerializer

class AdvancedSearchBook_View(APIView):
    def get(self, request, format=None):
        data={
            "Publisher":"Publisher",
            "Author":"Author",
            "Supplier":"Supplier"
        }
        return Response({'info':'SearchList','data':data}, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        search_option=request.data.get('search_option')
        search_data = request.data.get('search_input')

        if not search_data or not search_option:
            return Response({"error": "search_data and search_option are required."}, status=status.HTTP_400_BAD_REQUEST)






        

        


