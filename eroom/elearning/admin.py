from django.contrib import admin
from elearning.models import OnlineCourse,VideoClip,Member,UserType,Payment, User, Payment

class UserTypeAdmin(admin.ModelAdmin):
    def get_id(self):
        return f"{self.id} {self.usertype}"
    list_display = ("id", "usertype", get_id)

class OnlineCourseAdmin(admin.ModelAdmin):
    def get_id_course(self):
        return f"{self.id} "
    list_display = ("title", "published_date", get_id_course)

admin.site.register(OnlineCourse, OnlineCourseAdmin)
admin.site.register(VideoClip)
admin.site.register(Member)
admin.site.register(UserType, UserTypeAdmin)
admin.site.register(User)
admin.site.register(Payment)
