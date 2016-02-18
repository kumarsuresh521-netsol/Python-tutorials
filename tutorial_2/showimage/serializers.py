from rest_framework import serializers
from showimage.models import ShowImage

class ShowImageSerializer (serializers.ModelSerializer):
    class Meta:
        model = ShowImage
        fields = ('id', 'image_name', 'image_url')
#         pk = serializers.IntegerField(read_only=True)
#         image_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
#         image_url = serializers.ImageField()
#         
#         def create(self, validated_data):
#             return ShowImage.objects.create(**validated_data)
#         def update(self, instance, validated_data):
#             instance.image_name = validated_data.get('image_name', instance.image_name)
#             instance.image_url = validated_data.get('image_url', instance.image_url)