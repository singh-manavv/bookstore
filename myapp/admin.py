from django.contrib import admin
from .models import Contact,User,Book,Category

# Register your models here.
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Category)
