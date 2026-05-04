from django.db import models

class CustomOrder(models.Model):

    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    country = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)

    address = models.TextField(blank=True)

    order_type = models.CharField(max_length=100, blank=True)

    selected_pheta = models.CharField(max_length=200, blank=True)

    quantity = models.PositiveIntegerField(default=1)
    event_date = models.DateField()

    message = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name