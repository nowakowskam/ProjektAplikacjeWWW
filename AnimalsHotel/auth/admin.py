from django.contrib import admin
from .models import MyAccountManager, Users
# Register your models here.
admin.site.register(MyAccountManager)
admin.site.register(Users)