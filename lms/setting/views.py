from lms.setting.serializers import FineSettingSerializer,BookTypeSerializer
from lms.models import FineSetting,Book_Type

from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status



class FineSetting_View(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = FineSetting.objects.all()
    serializer_class = FineSettingSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class DeleteFineSetting_View(mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = FineSetting.objects.all()
    serializer_class = FineSettingSerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "FineSetting deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

    

class BookType_View(mixins.ListModelMixin,generics.GenericAPIView):

    queryset = Book_Type.objects.all()
    serializer_class = BookTypeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)    
