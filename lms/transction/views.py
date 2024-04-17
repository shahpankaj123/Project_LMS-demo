from lms.transction.serializers import TransactionSerializer,TransactionSerializer1
from lms.models import Transaction
from django.db import connection
from django.http import Http404


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class Transction_View(APIView):

    def get(self, request, format=None):
        data={
            'staff':'staff',
            'student':'student',
            'visitor':'visitor'
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

        




   