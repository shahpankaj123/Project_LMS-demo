from lms.transction.serializers import TransactionSerializer,TransactionSerializer1,BookListSerializer,ReturnbookSerializer
from lms.models import Transaction,Book,Student,Transaction,Staff,Visitor,FineSetting,CollectFine
from lms.models1 import CBSESchool
from django.db import connection
from django.http import Http404
from datetime import date
from datetime import datetime, timedelta
from django.db.models import Max


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError



class Transction_View(APIView):

    def get(self, request, format=None):
        data={
            'staff':'staff',
            'student':'student',
            'visitor':'visitor',
        }
        return Response({'data':data},status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        borrower_type=request.data['borrower_type']
        borrower_id=request.data['borrower_id']


        if borrower_id and borrower_type is  None:
            return Response({'message':'Error'},status=status.HTTP_400_BAD_REQUEST)
        
        try:
            if borrower_type=="student":
               book_obj = Transaction.objects.filter(student=borrower_id,school_id=1)
               borrower_obj = Transaction.objects.filter(student=borrower_id,school_id=1).first()
            elif borrower_type=='staff':
                book_obj = Transaction.objects.filter(staff=borrower_id,school_id=1)
                borrower_obj = Transaction.objects.filter(student=borrower_id,school_id=1).first()
            else:
                book_obj = Transaction.objects.filter(visitor=borrower_id,school_id=1)
                borrower_obj  = Transaction.objects.filter(student=borrower_id,school_id=1).first()
            if not book_obj.exists():
                return Response({"message": "book Data not found"}, status=status.HTTP_404_NOT_FOUND)
            if not borrower_obj:
                return Response({"message": "borrower Data not found"}, status=status.HTTP_404_NOT_FOUND)
        except Transaction.DoesNotExist:
            return Response({"message": "Data not found"}, status=status.HTTP_404_NOT_FOUND) 
        
        serializer = TransactionSerializer1(book_obj,many=True)
        serializer1 = TransactionSerializer(borrower_obj)

        return Response({'data1':serializer1.data,'data2':serializer.data}, status=status.HTTP_200_OK) 

        
class AdvancedSearchBook_View(APIView):
    data={
            "publisher":"publisher",
            "author":"author",
            "supplier":"supplier",
        }
    def get(self, request, format=None):
        return Response({'info':'SearchList','data':self.data}, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        search_option=request.data.get('search_option')
        search_data = request.data.get('search_input')

        if not search_data or not search_option:
            return Response({"error": "search_input and search_option are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        if search_option== "accession_number":
            books = Book.objects.get(school_id=1,accession_number=search_data,status=True)
            book_serializer = BookListSerializer(books)
            return Response({'info':'Success','data':book_serializer.data}, status=status.HTTP_200_OK)
        
        for value in self.data.values():
            if value == search_option:  
                filter_kwargs = {f'{value}__name__icontains': search_data}
                books = Book.objects.filter(**filter_kwargs,school_id=1,status=True)
                book_serializer = BookListSerializer(books,many=True)
                return Response({'info':'Success','data':book_serializer.data}, status=status.HTTP_200_OK)
            
        raise ValidationError("Search option not found")  

class IssuedBook_View(APIView):
    def post(self, request, pk, format=None):
        data = request.data

        if 'id' not in data or 'user_type' not in data or 'issue_date' not in data:
            return Response({"error": "Please provide user id , user type and issue date"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            issue_datetime = datetime.strptime(data['issue_date'], '%Y-%m-%d')
        except ValueError:
            return Response({"error": "Invalid issue datetime format. Please provide datetime in YYYY-MM-DD format."}, status=status.HTTP_400_BAD_REQUEST)
        
        issue_date = issue_datetime.date()
        try:
            book = Book.objects.get(school_id=1,accession_number=pk,status=True)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        
        user_type = data['user_type']
        user_id = data['id']
        try:
            if user_type == 'student':
                user = Student.objects.get(SchoolID=1, StudentID=user_id)
                due_date = issue_date + timedelta(days=14)
            elif user_type == 'staff':
                user = Staff.objects.get(school_id=1,library_id=user_id)
                due_date = issue_date + timedelta(days=30)  
            elif user_type == 'visitor':
                user = Visitor.objects.get(school_id=1,id=user_id)  
                due_date = issue_date + timedelta(days=30)
            else:
                return Response({"error": "Invalid user type"}, status=status.HTTP_400_BAD_REQUEST)
        except (Student.DoesNotExist, Staff.DoesNotExist, Visitor.DoesNotExist):
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            school = CBSESchool.objects.get(SchoolID=1)
        except CBSESchool.DoesNotExist:
            return Response({"error": "School not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Create transaction
        filter_kwargs = {f'{user_type}': user}
        transaction = Transaction.objects.create(**filter_kwargs, school_id=school, book=book, issue_date=issue_date,due_date=due_date,issue_type='New')
        book.status=False
        book.save()    
        return Response({"success": "Book issued successfully"}, status=status.HTTP_201_CREATED)


class ReturnBook_View(APIView):
    def get(self, request, pk, format=None):
        data2={}
        try:
            self.obj = Transaction.objects.get(school_id=1,book=pk,return_status='N')
        except Transaction.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer=ReturnbookSerializer(self.obj)

        try:
            self.obj1 =  FineSetting.objects.filter(book_type__name=serializer.data['book']['book_type_name']).latest('date')
            print(self.obj1)
        except FineSetting.DoesNotExist:
            return Response({"error": "Fine not found"}, status=status.HTTP_404_NOT_FOUND)

        issue_date = datetime.strptime(serializer.data['issue_date'], "%Y-%m-%d")
        due_date = datetime.strptime(serializer.data['due_date'], "%Y-%m-%d") 

        data2['no_of_days']= (due_date - issue_date).days
        data2['return_date'] = datetime.today().date()

        extended_date = datetime.strptime(str(data2['return_date']), "%Y-%m-%d")

        data2['extended_date']=(extended_date-due_date).days
        data2['total_days']=data2['extended_date']+data2['no_of_days']
        if self.obj1:
          data2['fine_amt']=self.obj1.fine_amt
        else:
            data2['fine_amt']=0

        print(data2)

        return Response({"data1":serializer.data,'data2':data2}, status=status.HTTP_200_OK)
    
    def post(self, request, pk, format=None):
        data = request.data  

        if 'return_date' not in data or 'total_fine' not in data or 'remark' not in data:
            return Response({"error": "Please provide return_date,total_fine,remark"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
          self.obj = Transaction.objects.get(school_id=1, book=pk, return_status='N')
          book=Book.objects.get(accession_number=pk)
        except Transaction.DoesNotExist:
          return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND) 
    
        serializer = ReturnbookSerializer(self.obj)

        try:
          self.obj1 = FineSetting.objects.filter(book_type__name=serializer.data['book']['book_type_name']).latest('date')
        except FineSetting.DoesNotExist:
          return Response({"error": "Fine not found"}, status=status.HTTP_404_NOT_FOUND)
    
        self.obj.return_status = 'Y'
        self.obj.return_date = data['return_date']

        self.obj.save()
        book.status=True
        book.save()      
        CollectFine.objects.create(transction_id=self.obj, fine=self.obj1, total_fine=data['total_fine'], remark=data['remark'])
        return Response({"data1": "Return Book Successful"}, status=status.HTTP_200_OK)
        







        

