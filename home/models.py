from django.db import models


class ImagesData(models.Model):
    image = models.ImageField(upload_to="Images")
    
    def get(self):
        return self.image.url


class FormData(models.Model):
    date = models.DateField()
    WO_ID = models.CharField(max_length=5000)
    customer = models.CharField(max_length=5000)
    job = models.CharField(max_length=5000)
    contractor = models.CharField(max_length=5000)
    inTime = models.CharField(max_length=5000)
    outTime = models.CharField(max_length=5000)
    totalTime = models.CharField(max_length=5000)
    job_description = models.TextField()
    waht_was_completed = models.TextField()
    still_needs_completed = models.TextField()
    issues = models.TextField()
    signature = models.ImageField(upload_to="Signatures")
    uploaded_images = models.ManyToManyField(ImagesData)

    def add_uploaded_image(self, image):
        uploaded_image = ImagesData.objects.create(image=image)
        self.uploaded_images.add(uploaded_image)
