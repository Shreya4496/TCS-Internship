from django.contrib import admin
from .models import *


admin.site.register(Complaint)
admin.site.register(Client)
admin.site.register(Service)
admin.site.register(Company)
admin.site.register(SLA)
# Register your models here.
