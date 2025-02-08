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
from myapp import views as stock_view 
from ebook import views as ebook_view 
from blog import views as blog_view
from django.urls import include

from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    #path("", elearning_view.home, name="home"),
    #path("home/", elearning_view.home, name="home"),
    path("aboutp/", elearning_view.aboutp, name="about page"),
    path("contactp/", elearning_view.contactp, name="contact page"),
    
    path("analyticlab/",elearning_view.analytics_lab, name="analytics"),
    #path("stock/<str:stock>/",stock_view.plot_line, name="plotline"),
    
    path("api/", include("vroom.urls")),
    #path("elearning/", include("elearning.urls")),
    #Topic 2.3.2
    path("admin/", admin.site.urls),
    path("currentday/", vroom_view.current_datetime, name="currentday"),
    
    path("daytemplate/", vroom_view.current_datetime_template, name="daytemplate"),
    path("listcourse/", elearning_view.ListCourseView.as_view(), name="listcourse"),
    path("register/", elearning_view.register_fill, name="registermember"),
    path("manageauthor/", vroom_view.authorformset, name="authorformset"),
    path("manageauthor_m/", vroom_view.authorformsetm, name="authorformsetm"),
    
    path("inquiry/", elearning_view.inquiry_fill, name="inquiry"),
    path("authorform/", vroom_view.author_fill, name="addauthor"),
    path("approveform/", elearning_view.approve_fill, name="approve"),
    path("loginsys/", elearning_view.login_fill, name="login"),
    path("logoutsys/", elearning_view.logout, name="logout"),
    path("memberpage/", elearning_view.ListMyCourse, name="mycourse"),
    path("inquiryform/", vroom_view.inquiry_fill, name="inquiryform"),
    path("courseroom/<int:courseid>/<int:videoid>/", elearning_view.course_room, name="courseroom"),
    path("payment/<int:courseid>/", elearning_view.payment_fill, name="payment"),
    path("courseapprove/", elearning_view.courseapprove_fill, name="approvecourse"),
    path("adminpage/", elearning_view.admin_manage, name="adminpage"),
    path("coursedemoroom/<int:courseid>/<int:videoid>/", elearning_view.coursedemo_room, name="coursedemoroom"),
    path("allcourse/",elearning_view.redirectView.as_view(), name="allcourse"),
    path("createcourse/",elearning_view.create_course, name="createcourse"),
    path("editcourse/<int:courseid>/",elearning_view.edit_course, name="editcourse"),
    path("approvepublish/",elearning_view.approve_course, name="publishcourse"),
    
    path("createvideo/<int:courseid>/",elearning_view.create_video, name="createvideo"),
    
    path("getauthor/<int:authorid>/",vroom_view.author_detail, name="getauthor"),
    
    path("listcreatedcourse/",elearning_view.list_created_course, name="listcreatedcourse"),
    path("editvideoclip/<int:courseid>/<int:videoid>/",elearning_view.edit_videoclip, name="editvideo"),

    path("aboutus/",vroom_view.aboutus.as_view(),name="aboutus"),
    path("courselist/",vroom_view.course_list.as_view(),name="course_list"),
    path("author_video/",vroom_view.author_video.as_view(),name="author_video"),

    path("delcourse/<int:courseid>/",elearning_view.del_course,name="deletecourse"),
    path("listvideo/<int:courseid>/",elearning_view.list_created_video,name="listvideo"),
    path("delvideo/<int:videoid>/",elearning_view.del_video,name="deletevideo"),
    
    path("api/onlinecourse/",elearning_view.ListOnlineCourseAPI.as_view(), name="querycourse"),
    path("sql/",vroom_view.sql_example.as_view(), name="sql"),
    path("<pk>/deletecourse/",elearning_view.course_delete_view.as_view(), name="del-course-view"),
    path("memberlist/",vroom_view.member_list, name="listmember"),
    path("canbeauthor/",vroom_view.member_author, name="canbeauthor"),
    path("adminlist/",vroom_view.member_admin, name="listadmin"),
    path("<pk>/listmemberm/", elearning_view.ShowMember.as_view(), name="membermix"),
    path("listvideo/", vroom_view.ListVideoView.as_view(), name="listvideo"),
    path("<slug:slug>", vroom_view.ListEachVideoView.as_view(), name="listvideoslug"),  # new
    #path("api/video/", vroom_view.VideoAPI.as_view(),name="videoapi"),
    path("stock/", include("vroom.urls")),
    path("settings/", elearning_view.setting_info, name="setting"),
    path("videoform/", vroom_view.video_fill, name="videoform"),
    path("jsexample/", vroom_view.jsexample, name="jsexample"),
    
  #  path("getsheet/<str:stock>/<str:startdate>/<str:enddate>/<int:day>/<str:attinfo>/<str:graphtype>/<str:mlgraph>/", stock_view.sheet_stock.as_view(), name = "getsheet" ),
    path("getsheet/", stock_view.sheet_stock.as_view(), name = "getsheet" ),
    path("viewplot/<str:report_id>/", stock_view.show_plot, name = "showplot" ),
    path("subscribe/", stock_view.Subscription, name = "subscribe" ),
    path("tabview/<str:report_id>/<str:stock>/<str:startdate>/<str:enddate>/<int:day>/<int:fast>/<int:slow>/", stock_view.tab_view, name = "tabview" ),
    path("validate/", elearning_view.mymodel_view, name="validate") , 
    path("indicators/", stock_view.indicators, name="indicators"),  
    path('proof/', elearning_view.proofview, name="proof view"),
    path('interpret/<str:stock>/', stock_view.interpret_p1, name="interpretp1"),
    path('interpretrsi/<str:stock>/', stock_view.interpret_p2, name="interpretrsi"),
    path('workshop2_1/<str:stock>/<str:startdate>/<str:enddate>/', stock_view.workshop_2_1_view, name="interpretrsi"),
    path('workshop2_2/<str:stock>/<str:startdate>/<str:enddate>/', stock_view.workshop_2_2_view, name="interpretrsi"),
    path('workshop2_3/<str:stock>/<str:startdate>/<str:enddate>/', stock_view.workshop_2_3_view, name="interpretrsi"),
    path('workshop2_4/<str:stock>/<str:startdate>/<str:enddate>/<int:pchg>/', stock_view.workshop_2_4_view, name="interpretrsi"), 
    path('workshop2_5/<str:stock>/<str:startdate>/<str:enddate>/', stock_view.workshop_2_5_view, name="interpretrsi"), 
    path('workshop2_6/<str:stock>/', stock_view.workshop_2_6_view, name="interpretrsi"), 
    path('workshop2_7/<str:stock>/<str:startdate>/<str:enddate>/<int:lssma>/', stock_view.workshop_2_7_view, name="interpretrsi"), 
    path('workshop2_8/<str:stock>/<str:startdate>/<str:enddate>/<str:period>/', stock_view.workshop_2_8_view, name="interpretrsi"), 
    path('workshop2_9/<str:stock>/<str:startdate>/<str:enddate>/<str:timef>/', stock_view.workshop_2_9_view, name="interpretrsi"), 
    path('workshop2_10/<str:stock>/<str:startdate>/<str:enddate>/', stock_view.workshop_2_10_view, name="interpretrsi"), 
    path('next2u/', stock_view.sheet_next2u.as_view(), name="interpretrsi"), 
    path('pdfview/', ebook_view.pdf_view_django, name="ebook"), 
    path('profile/', elearning_view.myprofile, name="ebook"), 
    path('subscription/', elearning_view.mysubscription, name="ebook"), 
    path('ebook/', elearning_view.ebooklist, name="ebook"), 
    path('carloan/', elearning_view.carloan, name="ebook"), 
    path('login/', elearning_view.LoginAuthenAPI.as_view(), name="login"), 
    path('api-token-auth/', views.obtain_auth_token),
    path('login4/', elearning_view.Login4),
    path('parcel/',elearning_view.parcel),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/protected/', elearning_view.ProtectedView.as_view(), name='protected_view'),
    path('blog/', blog_view.PostList.as_view(), name='home'),
    path('<slug:slug>/blog/', blog_view.PostDetail.as_view(), name='post_detail'),
    path('summernote/', include('django_summernote.urls')),
]

handler404 = vroom_view.Handler_404
handler500 = vroom_view.Handler_500
handler403 = vroom_view.Handler_403
handler400 = vroom_view.Handler_400

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
