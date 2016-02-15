from rest_framework import serializers
from snippets.models import Snippet, Cms, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class CmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cms
        fields = ('id', 'title', 'website', 'image', 'description')

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')

    
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    
    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')