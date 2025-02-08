"""
URL configuration for eroom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from  vroom import views


from vroom import views as vroom_view
from elearning import views as elearning_view
from django.urls import include

from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("currentday/", vroom_view.current_datetime, name="currentday"),
    
    path("daytemplate/", vroom_view.current_datetime_template, name="daytemplate"),
    path("listcourse/", elearning_view.ListCourseView.as_view(), name="listcourse"),
    path("register/", elearning_view.register_fill, name="registermember"),
    path("manageauthor/", vroom_view.authorformset, name="authorformset"),
    
    path("inquiry/", elearning_view.inquiry_fill, name="inquiry"),
    path("authorform/", vroom_view.author_fill, name="addauthor"),
    path("approveform/", elearning_view.approve_fill, name="approve"),
    path("loginsys/", elearning_view.login_fill, name="login"),
    path("logoutsys/", elearning_view.logout, name="logout"),
    path("memberpage/", elearning_view.ListMyCourse, name="mycourse"),
    path("inquiryform/", vroom_view.inquiry_fill, name="inquiryform"),
    path("payment/<int:courseid>/", elearning_view.payment_fill, name="payment"),
    path("approvecpurse/", elearning_view.approve_course, name="approvecourse"),
    path("adminpage/", elearning_view.admin_manage, name="adminpage"),
    path("coursedemoroom/<int:courseid>/<int:videoid>/", elearning_view.coursedemo_room, name="coursedemoroom"),
    path("createcourse/",elearning_view.create_course, name="createcourse"),
    path("editcourse/<int:courseid>/",elearning_view.edit_course, name="editcourse"),
    path("approvepublish/",elearning_view.approve_course, name="publishcourse"),
    
    path("createvideo/<int:courseid>/",elearning_view.create_video, name="createvideo"),
    
    
    path("listcreatedcourse/",elearning_view.list_created_course, name="listcreatedcourse"),
    path("editvideoclip/<int:courseid>/<int:videoid>/",elearning_view.edit_videoclip, name="editvideo"),

    path("courselist/",vroom_view.course_list.as_view(),name="course_list"),
    path("author_video/",vroom_view.author_video.as_view(),name="author_video"),

    path("delcourse/<int:courseid>/",elearning_view.del_course,name="deletecourse"),
    #No this in the book
    #path("listvideo/<int:courseid>/",elearning_view.list_created_video,name="listvideo"),
    path("delvideo/<int:videoid>/",elearning_view.del_video,name="deletevideo"),
    
    path("videoform/", vroom_view.video_fill, name="videoform"),
  
]


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
