from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display in list
    search_fields = ('title', 'author')                     # Add search box
    list_filter = ('publication_year',)   
          
admin.site.register(Book, BookAdmin)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Display the custom fields in the admin list view and detail view
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
