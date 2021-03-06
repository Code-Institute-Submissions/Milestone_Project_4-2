from django.db import models

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Poster(models.Model):

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    isbn10 = models.CharField(max_length=10, null=True, blank=True)
    isbn13 = models.CharField(max_length=13, null=True, blank=True)
    name = models.CharField(max_length=254)
    author = models.CharField(max_length=254)
    description = models.TextField()
    description_full = models.TextField(null=True, blank=True)
    published = models.DateField(null=True, blank=True)
    publisher = models.CharField(max_length=254, null=True, blank=True)
    pages = models.IntegerField( null=True, blank=True)
    language = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    disc_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

