from django.contrib import admin

from .models import product

class productAdmin(admin.ModelAdmin):
	list_display=('name','typeID','num','price','sumPrice','discount','position','code','describe')
	search_fields=('name','typeID','position','code','describe')


admin.site.register(product,productAdmin)
		