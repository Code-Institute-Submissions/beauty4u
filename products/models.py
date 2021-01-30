from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254, unique=True, blank=False)

    def __str__(self):
        return self.name


class Brand(models.Model):
    brand = models.CharField(max_length=254, unique=True, blank=False)

    def __str__(self):
        return self.brand


class Product(models.Model):

    BOOLEAN_CHOICE = (
        (True, "Yes, This is a featured product!"),
        (False, "No")
    )

    STOCK_CHOICES = (
        (True, "In Stock"),
        (False, "Out of Stock!")
    )

    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey('Brand', null=True, blank=True,
                              on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2,
                                     null=True, blank=True)
    in_stock = models.BooleanField(choices=STOCK_CHOICES,
                                   default=True, null=True, blank=True)
    size = models.CharField(max_length=254, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    featured_product = models.BooleanField(choices=BOOLEAN_CHOICE,
                                           default=False, null=True,
                                           blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):

    class Meta:
        verbose_name_plural = 'Reviews'

    product = models.ForeignKey('Product', null=True,
                                blank=True, on_delete=models.SET_NULL)
    review = models.TextField(max_length=2000, null=True, blank=True)
    added_by = models.CharField(max_length=250, null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.review
