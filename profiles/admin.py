from django.contrib import admin
from .models import UserProfile, Contact, SiteReview, SubscribeEmail

class SubscribeEmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'created')

admin.site.register(UserProfile)
admin.site.register(Contact)
admin.site.register(SiteReview)
admin.site.register(SubscribeEmail, SubscribeEmailAdmin)