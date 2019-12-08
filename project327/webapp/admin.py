from django.contrib import admin
from .models import Requisition

# register our models on django admin
admin.site.register(Requisition)