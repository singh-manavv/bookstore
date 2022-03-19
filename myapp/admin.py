from django.contrib import admin
from .models import Contact,User,Books,Category

# Register your models here.
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(Books)
admin.site.register(Category)
