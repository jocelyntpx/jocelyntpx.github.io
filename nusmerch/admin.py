from django.contrib import admin
from .models import userInfo

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_number', 'user_email', 'faculty')

    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('user_number', 'user_name')
        return queryset

    user_info.short_description = 'Info'

admin.site.register(userInfo,UserProfileAdmin)
