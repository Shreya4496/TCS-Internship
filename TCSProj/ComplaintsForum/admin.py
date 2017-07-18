from django.contrib import admin
from .models import *


admin.site.register(Complaint)
admin.site.register(Client)
admin.site.register(Service)
admin.site.register(Company)
admin.site.register(SLA)
admin.site.register(Chat)
admin.site.register(Provider)
admin.site.register(ServiceSelected)
admin.site.register(Employee)


# Register your models here.
