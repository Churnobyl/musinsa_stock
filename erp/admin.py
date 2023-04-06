from django.contrib import admin
from .models import Stuff, Inbound, Outbound

admin.site.register(Stuff)
admin.site.register(Inbound)
admin.site.register(Outbound)