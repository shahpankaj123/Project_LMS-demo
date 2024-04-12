from lms.manage_member.serializers import StudentListSerializer
from lms.models import Student
from django.db import connection


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# student api
class StudentList_View(APIView):
 
    def get(self, request, format=None):
        students = Student.objects.all()
        serializer = StudentListSerializer(students, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class SingleStudent_View(APIView):
 
    def get(self, request, pk,format=None):
        try:
            students = Student.objects.get(id=pk)
            print(connection.queries)
        except Student.DoesNotExist:
            return Response({"message": "Student not found"}, status=status.HTTP_404_NOT_FOUND)   
        serializer = StudentListSerializer(students)
        return Response(serializer.data,status=status.HTTP_200_OK)    
    
class ActiveStudent_View(APIView):
 
    def get(self, request,format=None):
        try:
            students = Student.objects.filter(status=True)
        except Student.DoesNotExist:
            return Response({"message": "Student not found"}, status=status.HTTP_404_NOT_FOUND)   
        serializer = StudentListSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)   
    
class UpdateStatusStudent_View(APIView): 

    def put(self, request, pk, format=None):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({"message": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentListSerializer(instance=student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Staff Api

