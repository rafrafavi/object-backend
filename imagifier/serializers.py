from rest_framework import serializers
from .models import Image, Mask


class MaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mask
        fields = ['id', 'coordinates', 'label', 'confidence']


class ImageSerializer(serializers.ModelSerializer):
    masks = MaskSerializer(many=True, read_only=True)

    class Meta:
        model = Image
        fields = ['id', 'image', 'uploaded_at', 'masks']