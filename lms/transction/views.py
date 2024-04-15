from lms.transction.serializers import TransactionSerializer
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
        borrower_type=int(request.data['borrower_type'])
        borrower_id=int(request.data['borrower_id'])


        if borrower_id and borrower_type is  None:
            return Response({'message':'Error'},status=status.HTTP_400_BAD_REQUEST)
        
        try:
            obj = Transaction.objects.filter(borrower_type=1, borrower_id=borrower_id)
            if not obj.exists():
                return Response({"message": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        except Transaction.DoesNotExist:
            return Response({"message": "Data not found"}, status=status.HTTP_404_NOT_FOUND) 
        
        serializer = TransactionSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 

        




   