from django.contrib import admin

from .models import Domain, Subdomain

admin.site.register(Domain)
admin.site.register(Subdomain)
