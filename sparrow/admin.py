from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Post
# Register your models here.


#unregister groups
admin.site.unregister(Group)

# Mix profile info into User info
class ProfileInline(admin.StackedInline):
    model = Profile
    
#extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    # Just display username fields on admin page
    fields = ["username"]
    inlines = [ProfileInline]
    
# Unregister initial user
admin.site.unregister(User)
# reregister user and Profile
admin.site.register(User, UserAdmin)
#admin.site.register(Profile)
admin.site.register(Post)


