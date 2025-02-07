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
from django.urls import path
from  vroom import views    #Import view in vroom app to use in this page

urlpatterns = [
    path("admin/", admin.site.urls),
    path("currentday/", views.current_datetime),
    path("currentdatetime/", views.current_datetime_template),
    path("videoform/", views.video_fill, name="videoform"),
    path("thanks/", views.thanks, name="thanks"),
    path("video_view/<int:id>/<int:year>/", views.video_view, name="listvideo"),
    path("listvideo/", views.ListVideoView.as_view(), name="list_video"),
    path("courselist/", views.course_list.as_view(), name="courselist"),
    path("inquiryform/", views.inquiry_fill, name="inquiry"),
    path("listauthor/", views.ListAuthorView.as_view(), name="listauthor"),
    path("authorform/", views.author_fill, name="authorform"), 
    path("authorvideo/", views.author_video.as_view(), name="authorvideo"), 
    path("authorformset/", views.authorformset, name="authorformset"), 

]
