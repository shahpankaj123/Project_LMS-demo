from lms.Config.serializers import BarcodeSerializer,AuthorSerializer,PublisherSerializer,SupplierSerializer,SubjectSerializer,LanguageSerializer,EditorSerializer,Book_TypeSerializer,RemarkSerializer,LocationSerializer
from lms.models import Author,Publisher,Supplier,Subject,Language,Editor,Book_Type,Remark,Location,Book
from django.http import JsonResponse
import json

from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

class BarcodeImageView(generics.RetrieveAPIView):

    def post(self, request, *args, **kwargs):
        accession_start_no = request.data.get('accession_start_no')
        accession_end_no = request.data.get('accession_end_no')

        if accession_start_no is None or accession_end_no is None:
            return JsonResponse({'error': 'Start and end accession numbers are required'}, status=400)

        try:
            start_no = int(accession_start_no)
            end_no = int(accession_end_no)
        except ValueError:
            return JsonResponse({'error': 'Invalid accession number format'}, status=400)

        if start_no >= end_no:
            return JsonResponse({'error': 'Start accession number must be less than end accession number'}, status=400)

        barcodes = []
        for accession_no in range(start_no, end_no + 1):
             try:
                barcode_image = Book.objects.get(accession_number=accession_no)
                for i in range(0, 4):
                    barcodes.append({'id': accession_no, 'barcode_image': barcode_image.book_barcode_image.url})
             except Book.DoesNotExist:
                pass

        return JsonResponse({'barcodes': barcodes})

class RandomBarcodeImageView(generics.RetrieveAPIView): 

    def post(self, request, *args, **kwargs):
        data=request.data.get('accession_data')
        print(type(data))

        if data is None:
            return Response({'info': 'Accession data is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        '''try:
            python_data = json.loads(data)
            print(python_data)
        except json.JSONDecodeError:
            return Response({'info':'Invalid Json data'}, status=status.HTTP_400_BAD_REQUEST)'''
        
        barcodes = []
        for accession_no in data:
             try:
                barcode_image = Book.objects.get(accession_number=accession_no)
                for i in range(0,4):
                   barcodes.append({'id': accession_no, 'barcode_image': barcode_image.book_barcode_image.url})
             except Book.DoesNotExist:
                pass

        return JsonResponse({'barcodes': barcodes})
    
  
class CreateAuthor_View(mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({
                'status': 'success',
                'message': 'Author created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CreatePublisher_View(mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({
                'status': 'success',
                'message': 'Publisher created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateSupplier_View(mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({
                'status': 'success',
                'message': 'Supplier created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      

class CreateSubject_View(mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({
                'status': 'success',
                'message': 'Subject created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateLanguage_View(mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({
                'status': 'success',
                'message': 'Language created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateEditor_View(mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Editor.objects.all()
    serializer_class = EditorSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({
                'status': 'success',
                'message': 'Editor created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class CreateBook_Type_View(mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Book_Type.objects.all()
    serializer_class = Book_TypeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({
                'status': 'success',
                'message': 'Book_Type created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

class CreateRemark_View(mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Remark.objects.all()
    serializer_class = RemarkSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({
                'status': 'success',
                'message': 'Remark created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)               

class CreateLocation_View(mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({
                'status': 'success',
                'message': 'Location created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
