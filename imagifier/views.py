from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Image, Mask
from .serializers import ImageSerializer, MaskSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def perform_create(self, serializer):
        # Save the image
        image_instance = serializer.save()

        # Here you would normally call your object detection model
        # For demonstration, we'll create a dummy mask
        Mask.objects.create(
            image=image_instance,
            coordinates={
                "x": 100,
                "y": 100,
                "width": 50,
                "height": 50
            },
            label="example_object",
            confidence=0.95
        )