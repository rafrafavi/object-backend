from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id} uploaded at {self.uploaded_at}"

class Mask(models.Model):
    image = models.ForeignKey(Image, related_name='masks', on_delete=models.CASCADE)
    coordinates = models.JSONField()
    label = models.CharField(max_length=100)
    confidence = models.FloatField()

    def __str__(self):
        return f"Mask {self.id} for Image {self.image_id}"