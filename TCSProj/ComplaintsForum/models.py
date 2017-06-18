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


class Company(models.Model):
    company_name=models.CharField(max_length=50)
    company_location=models.CharField(max_length=50)
    point_of_contact=models.CharField(max_length=50)

    def __unicode__(self):  # __str__ for Python 3, __unicode__ for Python 2
        return self.company_name


class Service(models.Model):
     service_name=models.CharField(max_length=50)
     min_duration=models.CharField(max_length=50)
     offering_company=models.ForeignKey(Company, on_delete=models.CASCADE)
     service_objective=models.CharField(max_length=1000)
     service_description=models.CharField(max_length=5000)

     def __unicode__(self):  # __str__ for Python 3, __unicode__ for Python 2
         return self.service_name

class Client(models.Model):
    client_name=models.CharField(max_length=50)
    client_company=models.CharField(max_length=50)
    client_email=models.EmailField()
    client_contact=models.CharField(max_length=12)

    def __unicode__(self):  # __str__ for Python 3, __unicode__ for Python 2
        return self.client_name
class SLA(models.Model):
    service_name = models.ForeignKey(Service, on_delete=models.CASCADE)
    min_duration = models.ForeignKey(Service, on_delete=models.CASCADE)
    service_id= models.ForeignKey(Service, on_delete=models.CASCADE)
    company_name=models.ForeignKey(Company, on_delete=models.CASCADE)
   # vendor=models.ForeignKey(Company, on_delete=models.CASCADE)
    point_of_contact=models.CharField(max_length=50)
    client_name=models.ForeignKey(Client, on_delete=models.CASCADE)
    service_date = models.DateField()
    target_audience=models.CharField(max_length=500)
    service_objective=models.CharField(max_length=5000)
    performance_parameter=models.CharField(max_length=5000)
    performance_measure=models.CharField(max_length=5000)
    service_hours=models.CharField(max_length=50)
    schedule=models.CharField(max_length=50)


    def __unicode__(self):  # __str__ for Python 3, __unicode__ for Python 2
        return self.service_name



from django.contrib.auth.models import User

class Chat(models.Model):
    #created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    message = models.CharField(max_length=200)

    def __unicode__(self):
        return self.message

    def empty():
        pass






