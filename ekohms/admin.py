from ekohms.models import User, Receptionist
from django.contrib import admin
from .models import *

from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    list_display = ('username','email', 'phone','is_staff','created_at','updated_at' )
    search_fields =('username','email')
    readonly_fields = ['created_at','updated_at']

    filter_horizontal =()
    list_filter =()
    fieldsets =()

admin.site.register(User,AccountAdmin)
admin.site.register(Receptionist)
admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(RoomStatus)

