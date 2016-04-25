from django.contrib import admin
from portal.models import Book
from portal.models import BookCategory

# Register your models here.

admin.site.register(Book)
admin.site.register(BookCategory)

