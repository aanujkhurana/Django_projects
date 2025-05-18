from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('new', 'New'), ('in_progress', 'In Progress'), ('resolved', 'Resolved')], default='new')
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return(f"{self.firstname} {self.lastname}")