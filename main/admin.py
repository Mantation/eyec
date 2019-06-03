from django.contrib import admin
from .models import Messages


#admin.site.site_header = "eyeC Administration"

class ClientMessageAdmin(admin.ModelAdmin):
    list_display = ("profile","email","message")

    def profile(self,obj):
        return obj.firstname + ' ' + obj.lastname

admin.site.register(Messages,ClientMessageAdmin)
