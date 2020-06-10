from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import userInfo
from .forms import UserForm, UserProfileForm

# Register your models here.
"""class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'email', 'faculty','image',
    	'matric','major','campus_residential_type',]
    login_form = UserForm
    signup_form = UserProfileForm
    model = userInfo


admin.site.register(userInfo,UserProfileAdmin)"""


"""class ProfileInline(admin.StackedInline):
    model = userInfo
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'email', 'faculty','image',
        'matric','campus_residential_type',]

    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('matric')
        return queryset

    user_info.short_description = 'Info'

admin.site.register(userInfo,UserProfileAdmin)"""

admin.site.register(userInfo)
admin.site.register(Post)