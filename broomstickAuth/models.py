from django.db import models

# Create your models here
class Note(models.Model):
    productName = models.CharField(max_length=50, default="")
    tagline = models.CharField(max_length=50, default="")
    companyName = models.CharField(max_length=50, default="")
    productDescription = models.CharField(max_length=50, default="")
    productImageUrl = models.CharField(max_length=50, default="")
    featured = models.CharField(max_length=50, default="")
    # productImage = models.ImageField(upload_to='uploads', default="")
    # def __str__(self):
    #     return self.productName
    #     return self.companyName