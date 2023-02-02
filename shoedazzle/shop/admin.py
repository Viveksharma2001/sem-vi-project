from django.contrib import admin
from shop.models import Contact

# Register your models here.
from .models import Customer, product
admin.site.register(product),



# Register your models here.
admin.site.register(Contact)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','zipcode','state']
