from showimage.models import ShowImage
from showimage.serializers import ShowImageSerializer
from rest_framework import generics

# Create your views here.
class ShowImageList(generics.ListCreateAPIView):
    queryset = ShowImage.objects.all()
    serializer_class = ShowImageSerializer
    
class ShowImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShowImage.objects.all()
    serializer_class = ShowImageSerializer