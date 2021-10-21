from django.db import models

class Bookings(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length =30)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
    phone_no = models.CharField(max_length =15)
    postal_address = models.CharField(max_length =30)
    city = models.CharField(max_length =30, default='Nairobi', editable=False)
    servicies = models.CharField(max_length =30)
    comments = models.CharField(max_length =500)

    def save_bookings(self):
        self.save()

    def update_bookings(self):
        self.save()

    def delete_bookings(self):
        self.delete()






