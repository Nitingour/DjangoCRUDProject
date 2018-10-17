from django.contrib import admin
from ViewApp.models import Book
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display=['bookname','author','price','publisher']

admin.site.register(Book,BookAdmin)
