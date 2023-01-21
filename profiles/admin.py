from django.contrib import admin
from .models import UserProfile, Contact, SiteReview

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Contact)
admin.site.register(SiteReview)