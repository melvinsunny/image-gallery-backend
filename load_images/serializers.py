from rest_framework import serializers
from .models import *

class ImageDetailSerializer(serializers.ModelSerializer):
    short_description = serializers.SerializerMethodField()
    short_title = serializers.SerializerMethodField()

    class Meta:
        model = ImageDetail
        fields = ["id","title","short_title","description","short_description","image_url"]

    def get_short_title(self,obj):
        if len(obj.title) >= 27:
            return obj.title[:26] + ' ...'
        else:
            return obj.title

    def get_short_description(self,obj):
        if len(obj.description) >= 30:
            return obj.description[:29] + ' ...'
        else:
            return obj.description