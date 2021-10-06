from django.db import models

class Bookings(models.Model):
    name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_no = models.IntegerField()
    postal_address = models.CharField(max_length =30)
    city = models.CharField(max_length =30, default='Nairobi', editable=False)
    servicies = models.CharField(max_length =30)
    comments = models.CharField(max_length =500)




