from django.db import models
# from django.utils import timezone

# Create your models here.


class Complaint(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    linked_company = models.CharField(max_length=1000)
    complaint_type = models.CharField(max_length=100)
    complaint_description = models.CharField(max_length=5000)

    def __unicode__(self):  # __str__ for Python 3, __unicode__ for Python 2
        return self.first_name
