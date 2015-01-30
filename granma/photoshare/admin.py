from django.contrib import admin

from photoshare.models import GroupRoleUser
from photoshare.models import Group
from photoshare.models import UserProfile
from photoshare.models import Photo

class GroupRoleUserAdmin(admin.ModelAdmin):
    pass

class GroupAdmin(admin.ModelAdmin):
    pass

class UserProfileAdmin(admin.ModelAdmin):
    pass

class PhotoAdmin(admin.ModelAdmin):
    pass

admin.site.register(GroupRoleUser, GroupRoleUserAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Photo, PhotoAdmin)