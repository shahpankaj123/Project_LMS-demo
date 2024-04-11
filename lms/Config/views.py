from lms.Config.serializers import BarcodeSerializer,AuthorSerializer,PublisherSerializer,SupplierSerializer,SubjectSerializer,LanguageSerializer,EditorSerializer,Book_TypeSerializer,RemarkSerializer,LocationSerializer
from lms.models import Author,Publisher,Supplier,Subject,Language,Editor,Book_Type,Remark,Location,Book

from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

class BarcodeImageView(generics.RetrieveAPIView):
    serializer_class = BarcodeSerializer

    def get_object(self):
        book_id = self.kwargs.get('pk')
        book = generics.get_object_or_404(Book, pk=book_id)
        if not book.book_barcode_image:
            return Response({"error": "No barcode image found for this book."}, status=status.HTTP_404_NOT_FOUND)

        return book
        
  
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
