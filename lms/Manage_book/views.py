from lms.Manage_book.serializers import Create_SeriesBookSerializer,BookSummary_UodateSerializer,BookListSerializer,BookImg_UpdateSerializer,BookImg_ListSerializer
from lms.models import Book
from django.db import connection
from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError


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
        
class UpdateBook_View(APIView):
    def get(self,request,pk,format=None):
        print(pk)
        try:
            book = Book.objects.get(accession_number=pk)
            print(book)
        except Book.DoesNotExist:
            return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = Create_SeriesBookSerializer(book)
        return Response({'info':'Success','data':serializer.data}, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        try:
            book = Book.objects.get(accession_number=pk)
        except Book.DoesNotExist:
            return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = Create_SeriesBookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'info': 'Book updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
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
    data={
            "publisher":"publisher",
            "author":"author",
            "supplier":"supplier",
            "accession_number":"accession_number"
        }
    def get(self, request, format=None):
        return Response({'info':'SearchList','data':self.data}, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        search_option=request.data.get('search_option')
        search_data = request.data.get('search_input')

        if not search_data or not search_option:
            return Response({"error": "search_input and search_option are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        if search_option== "accession_number":
            books = Book.objects.get(accession_number=search_data)
            book_serializer = BookListSerializer(books)
            return Response({'info':'Success','data':book_serializer.data}, status=status.HTTP_200_OK)
        
        for value in self.data.values():
            if value == search_option:
                filter_kwargs = {f'{value}__name__icontains': search_data}
                books = Book.objects.filter(**filter_kwargs)
                book_serializer = BookListSerializer(books,many=True)
                return Response({'info':'Success','data':book_serializer.data}, status=status.HTTP_200_OK)
            
        raise ValidationError("Search option not found")    
    
class BookImg_UodateView(APIView):

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        accession_number = request.data.get('accession_number')
        if accession_number is None:
            return Response({"error": "accession_number not found in request data."}, status=status.HTTP_400_BAD_REQUEST)

        book = get_object_or_404(Book, accession_number=accession_number)

        book_serializer = BookImg_ListSerializer(book)
        return Response({'info':'Success','data':book_serializer.data}, status=status.HTTP_200_OK)
    
    def put(self, request, format=None):

        existing_image = Book.objects.filter(accession_number=request.data.get('accession_number')).first() 

        serializer =BookImg_UpdateSerializer(existing_image,data=request.data)
        if serializer.is_valid():
            if Book.objects.exists():
                # Delete the existing image
                previous_image = Book.objects.first()
                previous_image.book_image.delete(save=False)
            serializer.save()
            return Response({'info':'Success','data':serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
                
                
                









        

        


