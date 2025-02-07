from django.shortcuts import render
from django.http import HttpResponse

import datetime
#Function view
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def video_view(request, id, year):  # แก้ไขเมื่อต้องการส่งเออร์กูเมนต์ให้กับพาธหน้า 44
    v = Video.objects.get(id=id, published_date__contains=year)    # Get ฟังก์ชันดึงข้อมูลจะได้ข้อมูลหนึ่งอ็อบเจกต์
    return render(request,"video_view.html", {"video": v} )

from django.template import loader
def current_datetime_template(request):
    now = datetime.datetime.now()
    template = loader.get_template("daytemplate.html") 
    context = { "now": now} 
    return HttpResponse(template.render(context, request))
# Loader will be deprecated soon. 
# You can use  
# return  render(request, “daytemplate.html”, context)
# Please add path to this function view
def thanks(request):
    return render(request, 'thanks.html')
                  
#Function view calles form
from .forms import VideoForm    #Using .forms means vroom.forms
from .models import Video
def video_fill(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = VideoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
           # create data of Video model
            v = Video(title= form.cleaned_data['video_title'],          #Clean data received by VideoForm form
                  published_date= form.cleaned_data['video_publish'])
            v.save()
            context = { "title": v.title, "published_date": v.published_date   } 
            template = loader.get_template("thanks.html") 
            return HttpResponse(template.render(context, request))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = VideoForm()
    return render(request, "videoform.html", {"form": form})

from django.views.generic.base import TemplateView
#Class-based view using TemplateView
class ListVideoView(TemplateView):
    template_name = "listvideo.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_video"] = Video.objects.all()
        return context

from django.views.generic.list import ListView
#Class-based view using ListView

class course_list(ListView):
    model = Video   #ในหนังสือหน้า 49 model = Course นั้น Course ยังไม่ถูกสร้างให้แก้เป็น Video ก่อน
    #template จะอนู่ใน Folder template/vroom/video_list.html

from .forms import InquiryForm
#Function view 
def inquiry_fill(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = InquiryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #...Send email...
            return HttpResponse('Thanks....Sent email already.')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = InquiryForm()

    return render(request, "inquiryform.html", {"form": form})

#Class-based view 
from .models import Author
class ListAuthorView(TemplateView):
    template_name = "author.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["authors"] = Author.objects.all()
        return context


#การสร้างวิวสำหรับกรอกข้อมูล Author ซึ่งเรียกใ้ช้ Model form 
#หน้า 66
from .forms import AuthorForm
def author_fill(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = AuthorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            a = Author(id=form.cleaned_data['id'],
		firstname = form.cleaned_data['firstname'], 
		lastname= form.cleaned_data['lastname'],
		phone= form.cleaned_data['phone'], 			
		joined_date=form.cleaned_data['joined_date'])
            a.save()
            context = {"id":a.id, "firstname": a.firstname, 
		"lastname": a.lastname, "phone": a.phone,
		"joined_date": a.joined_date } 
            template = loader.get_template("thanksauthor.html") 
            return HttpResponse(template.render(context, request))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AuthorForm()
    return render(request, "authorform.html", {"form": form})

#One view multiple forms
#หน้า 76
class author_video(TemplateView):
    template_name = 'author_video.html'

    def post(self, request, *args, **kwargs):
        formauthor = AuthorForm(request.POST)
        formvideo = VideoForm(request.POST)
        if formauthor.is_valid() and formvideo.is_valid():
        
            addauthor = Author(id = formauthor.cleaned_data['id'],
                            firstname = formauthor.cleaned_data['firstname'], 
                            lastname= formauthor.cleaned_data['lastname'],
                            joined_date = formauthor.cleaned_data['joined_date'], 
                            phone = formauthor.cleaned_data['phone']
                       )
           
            addauthor.save()
            video = Video(title= formvideo.cleaned_data['title'], published_date = formvideo.cleaned_data['published_date'],
                          author = addauthor)
            video.save()
            return render(request, "thankssave.html" )
        else:
            print (formauthor.is_valid())   #form contains data and errors
            print (formauthor.errors)
            print (formvideo.is_valid())   #form contains data and errors
            print (formvideo.errors)
            return render(request, "errorform.html" )   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formauthor"] = AuthorForm()
        context["formvideo"] = VideoForm()
        
        return context
#Function-based view for form set หน้า 77

from django.forms import modelformset_factory
from django.shortcuts import render
#Example form ser view
def authorformset(request):
    AuthorFormSet = modelformset_factory(Author, form = AuthorForm ,  extra=1)
    if request.method == "POST":
        formset = AuthorFormSet(request.POST)
        if formset.is_valid():
           formset.save()
            #This could be template
        return HttpResponse('Thanks....Save formset already.')
    else:
        formset = AuthorFormSet()
        
    return render(request, "addauthors.html", {"formset": formset})    
