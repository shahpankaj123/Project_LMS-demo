from lms.manage_member.serializers import StudentListSerializer,StaffSerializer,VisitorSerializer
from lms.models import Student,Staff,Visitor
from django.db import connection
from django.http import Http404


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

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
        

#staff api

class CreateListStaff_View(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
        

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({
                'status': 'success',
                'message': 'Staff created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UpdateStaff_View(mixins.ListModelMixin,mixins.UpdateModelMixin,
                  generics.GenericAPIView):
  serializer_class = StaffSerializer
  def get(self, request,pk, *args, **kwargs):
    try:
        instance = Staff.objects.get(library_id=pk)
    except Staff.DoesNotExist:
        raise Http404("Staff does not exist")

    serializer = self.get_serializer(instance)
    return Response({
            'status': 'success',
            'message': 'Staff Got successfully',
            'data': serializer.data
        },status=status.HTTP_200_OK)
  
  def put(self, request,pk, *args, **kwargs):
    try:
        instance = Staff.objects.get(library_id=pk)
    except Staff.DoesNotExist:
        raise Http404("Staff does not exist")

    serializer = self.get_serializer(instance, data=request.data)
    if serializer.is_valid():
        self.perform_update(serializer)
        return Response({
            'status': 'success',
            'message': 'Staff updated successfully',
            'data': serializer.data
        },status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
# Visitor Api
class CreateListVisitor_View(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
        

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({
                'status': 'success',
                'message': 'Visitor created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
class UpdateVisitor_View(mixins.ListModelMixin,mixins.UpdateModelMixin,
                  generics.GenericAPIView):    
    
    serializer_class = VisitorSerializer
    def get(self, request,pk, *args, **kwargs):
        try:
            instance = Visitor.objects.get(id=pk)
        except Visitor.DoesNotExist:
            raise Http404("Staff does not exist")

        serializer = self.get_serializer(instance)
        return Response({
            'status': 'success',
            'message': 'Visitor Got successfully',
            'data': serializer.data
        },status=status.HTTP_200_OK)
  
    def put(self, request,pk, *args, **kwargs):
        try:
            instance = Visitor.objects.get(id=pk)
        except Visitor.DoesNotExist:
            raise Http404("Staff does not exist")

        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
           self.perform_update(serializer)
           return Response({
            'status': 'success',
            'message': 'Visitor updated successfully',
            'data': serializer.data
        },status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class List_InActiveVisitor_View(mixins.ListModelMixin,
                  generics.GenericAPIView):  
    
    serializer_class = VisitorSerializer
    def get(self, request, *args, **kwargs):
        try:
            instance = Visitor.objects.filter(status=False)
        except Visitor.DoesNotExist:
            raise Http404("Staff does not exist")

        serializer = self.get_serializer(instance,many=True)
        return Response({
            'status': 'success',
            'message': 'InActtive Visitor',
            'data': serializer.data
        },status=status.HTTP_200_OK)

class List_GuestVisitor_View(mixins.ListModelMixin,
                  generics.GenericAPIView):  
    
    serializer_class = VisitorSerializer
    def get(self, request, *args, **kwargs):
        try:
            instance = Visitor.objects.filter(membership_type='Guest_Visistor')
        except Visitor.DoesNotExist:
            raise Http404("Guest does not exist")

        serializer = self.get_serializer(instance,many=True)
        return Response({
            'status': 'success',
            'message': 'Guest Visitor',
            'data': serializer.data
        },status=status.HTTP_200_OK)      