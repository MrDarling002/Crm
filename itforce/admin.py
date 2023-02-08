from django.contrib import admin
from.models import Customer, OrderStatus,Service,ProductBrand,ProductCategory,Order

admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Service)
admin.site.register(ProductBrand)
admin.site.register(ProductCategory)
admin.site.register(OrderStatus)



