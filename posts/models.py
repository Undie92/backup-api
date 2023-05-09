from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):


    CATEGORY_TYPES = (
        ("food", "Food"),
        ("drink", "Drink"),
        ("toys", "Toys"),
        ("technology", "Technology"),
        ("sports", "Sports"),
        ("clothing", "Clothing"),
        ("footwear", "Footwear"),
        ("household", "Household"),
        ("homeware", "Homeware"),
        ("jewellery", "Jewellery"),
        ("diy", "DIY"),
        ("accessories", "Accessories"),
        ("other", "Other")
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category_type = models.CharField(max_length=50, choices=CATEGORY_TYPES)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_mzgj1g', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_filter = models.CharField(
        max_length=32, default='normal'
        )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
