
import smtplib

from django.template import Context, Template
from datetime import  date, timedelta
from django.views.generic.base import TemplateView
from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseServerError,HttpResponseForbidden
from elearning.models import OnlineCourse, Member,UserType, Payment, VideoClip
from elearning.forms import RegisterForm, InquiryForm, LoginForm, ApproveForm, CourseApproveForm, CourseForm,ApproveCourseForm
from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session

# Create your views here.
#Use case: Login
def login_fill(request):
    #1 if this is a POST request we need to process the form data
    if request.method == "POST":
       form = LoginForm(request.POST)
       if form.is_valid():	
           m = Member.objects.get(userlogin=request.POST["loginuser"])  
	#2 Check password  
           if m.check_password(request.POST["loginpass"]):
                #create session info for client
                request.session["member_id"] = m.id
                request.session["member_firstname"] = m.firstname
                #store info in session database
                s = SessionStore()
                s.create()   #Create new session, get session key
                keysession = s.session_key
                request.session["session_key"] = keysession
                s = SessionStore(s.session_key)   #Store in DB
                s['member_id'] = m.id
                s['member_firstname'] = m.firstname
                #check if the same session
                #query from store session db
                s = Session.objects.get(pk= keysession)
                s.session_data    #data is encoded.
               #3 Check type  
                utype1 = UserType.objects.get(usertype = "Mem")
                utype2 = UserType.objects.get(usertype = "Admin")
                if (m.usertype == utype1):  #Member
                    path = "../listcourse/"

                    from django.shortcuts import redirect, render #บางที Django ก็ลืมไลบรารี

                    return redirect(path) 
                elif (m.usertype == utype2): #Admin
                    from django.shortcuts import redirect, render
                    path = "../adminpage/" 
                    return redirect(path)
                else:
                    path = "../listcourse/" 
                    redirect(path)
           else:
                return HttpResponse("Sorry...you don't have right to access this system.")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()
    from django.shortcuts import redirect, render
    return render(request, "login.html", {"form": form})


#Use case: Logout
def logout(request):
    try:
        member = request.session["member_firstname"]
        del request.session["member_id"]
        del request.session["member_firstname"]
        del request.session["session_key"]
                
    except KeyError:
        pass

    return redirect("../listcourse/")

#Use case: See course
class ListCourseView(TemplateView):
    def get(self, request):
        #check if member or others 
        latest_course = OnlineCourse.objects.all()
        
        if 'member_id' in request.session:
            return render(request, "listcoursemem.html", {"latest_course": latest_course})   
        else:
            return render(request, "listcourse.html", {"latest_course": latest_course}) 
#Use case: Demo course
def  coursedemo_room(request, courseid,videoid):
    #1 Find course
    c = OnlineCourse.objects.get(id=courseid)
    listv = []
    #2 Find video in the course using related_name - videoclip 
    for video in VideoClip.objects.filter(demo=True, videoclip__id = courseid):
        listv.append(video)
    context = Context()
    context['video_list'] = listv
    context['title'] = c.title
    context['briefdetail'] = c.briefdetail
    if videoid == 0:
        context['introclip'] = listv[0].fileclip
    else:
        v = VideoClip.objects.get(id = videoid )
        context['introclip'] = v.fileclip
        
    context['courseid'] = courseid
    #3 Rendering template
    if 'member_id' in request.session:
        context['usertype'] = True    #member
        return render(request, "demoroommem.html", {"context": context})
    else:
        return render(request, "demoroom.html", {"context": context})

#Use case: Ask info
from django.core.mail import send_mail
import smtplib 
def inquiry_fill(request):
   if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = InquiryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            try:
                message  = "From: "+request.POST['sender']+"<br/> Message:"+ request.POST['message']
                result = send_mail(
                    subject = request.POST['subject'],
                    message = message,
                    html_message = message,

                    from_email = "nextcodecamp@gmail.com",
                    recipient_list = ["nextcodecamp@gmail.com",request.POST['sender'] ],
                    fail_silently=False,
                )
            except smtplib.SMTPException:
                return HttpResponse("Can't send email. Please contact us in Facebook. Thanks.")
            return render(request, "emailthanks.html")
    # if a GET (or any other method) we'll create a blank form
   else:
        form = InquiryForm()

   return render(request, "askinfo.html", {"form": form})

#Use case: Register
from datetime import  date, timedelta
def register_fill(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            utype = UserType.objects.get(id= 1)
            member = Member(firstname= form.cleaned_data['firstname'],
                            lastname = form.cleaned_data['lastname'],
                            userlogin = form.cleaned_data['userlogin'],
                            userpass = form.cleaned_data['userpass'],
                            joined_date = date.today(), 
                            phone = form.cleaned_data['phone'],
                            usertype =utype,
                            expire_date = date.today() + timedelta(days=365),
                            approve = False)
            member.save()
            return render(request, "thanksregister.html")
    else:
        form = RegisterForm()

    return render(request, "registerform.html", {"form": form})
from datetime import  date, timedelta, datetime

#Use case: Buy course
def payment_fill(request, courseid):
    #1 check if member login or not
    if 'member_id' in request.session:
        member_id  = request.session['member_id']
    else:
        return render(request, "notifyregister.html") 
    course = OnlineCourse.objects.get(id=courseid)
    context = Context()
    context['course'] = course
    context['title'] = course.title
    context['saleprice'] = course.saleprice
    
    #2 get member object
    member = Member.objects.get(id = request.session['member_id'])
    context['member'] = member
    now = datetime.now()
    paydeadline = now.strftime("%Y-%m-%d %H:%M:%S")
    context['deadline'] = paydeadline
    #3 create payment record
    newpayment = Payment(pay_date = paydeadline, member= member, course = course , paidprice = course.saleprice, checkpaid = False)
    #4 rendering template 
    if newpayment :
        newpayment.save()
        return render(request, "paycourse.html", {"context":context})
    else:
        return HttpResponse('Error from payment')

def ListMyCourse(request):
    useraccess = request.session['member_id']
    username = request.session['member_firstname']
    usersessionkey  = request.session["session_key"]
    memberacc = Member.objects.get(id = useraccess)
    mycourse = Payment.objects.filter(member = memberacc, checkpaid = True)
    listcourse =[]
    #Outer loop
    for mc in mycourse:
        #Inner loop  
        for c in OnlineCourse.objects.all():
            if c == mc.course:
                listcourse.append(c)
    return render(request, "memberpage.html", {"mycourse": listcourse})

def list_created_course(request):
    useraccess = request.session['member_id']
    username = request.session['member_firstname']
    usersessionkey  = request.session["session_key"]
    courseowner  = Member.objects.get(id = useraccess)
    course = OnlineCourse.objects.filter(owner = courseowner )
    return render(request, "listcreatedcourse.html", {"course": course})

#Use case: Manage course
def handle_uploaded_file(f, owner, type):   
    with open('media/elearning/static/'+type+'/'+str(owner)+"_"+f.name, 'wb+') as destination:   
        for chunk in f.chunks(): 
            destination.write(chunk)   

def create_course(request): 
    if request.method == "POST":
        owner  = request.session['member_id']
        member = Member.objects.get(id = owner)
        # create a form instance and populate it with data from the request:
        form = CourseForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            handle_uploaded_file(request.FILES["cover"], owner,"img")
            #form.save()
            c = OnlineCourse(title= form.cleaned_data['title'], 
                             cover=  "elearning/static/img/"+str(owner)+"_"+request.FILES['cover'].name,
                             briefdetail = form.cleaned_data['briefdetail'],
                             saleprice= form.cleaned_data['saleprice'],
                             approve = False,
                             owner = member)
            c.save()
            path = "/listcreatedcourse/"    
            return redirect(path) 
        else:
             return render(request, "errorform.html", {'formerrors':form.errors})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CourseForm()
    return render(request, "createcourse.html", {"form": form})

#Use case: Manage course
def edit_course(request,courseid):
    from django.shortcuts import redirect, render
    if request.method == "POST":
        owner  = request.session['member_id']
        member = Member.objects.get(id = owner)
        # create a form instance and populate it with data from the request:
        form = CourseForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            c = OnlineCourse.objects.get(id = courseid)
            c.title= form.cleaned_data['title']
            c.briefdetail = form.cleaned_data['briefdetail']
            c.saleprice= form.cleaned_data['saleprice']
            c.save()
            return redirect("/listcreatedcourse/")
        else:
           return render(request, "errorform.html", {'formerrors': form.errors})
    # if a GET (or any other method) we'll create a blank form
    else:
        course = OnlineCourse.objects.get(id = courseid)
        form = CourseForm(instance = course)
    return render(request, "editcourse.html", {"form": form})

#Use case: Manage course
def del_course(request, courseid):
    useraccess = request.session['member_id']
    course = OnlineCourse.objects.get(id = courseid)
    course.delete()
    return render(request, "thanksdel.html")

from django.forms import BaseModelFormSet
#Use case: Manage course
def create_video(request, courseid):
    #1 Create session info for courseid
    if courseid != 0:
        request.session['create_courseid'] = courseid
    else:
        courseid = request.session['create_courseid']    
    #2 Submitted information      
    if request.method == "POST":
        form = VideoForm(request.POST)
        owner  = request.session['member_id']
        member = Member.objects.get(id = owner)
       
        if form.is_valid():
            handle_uploaded_file(request.FILES["fileclip"], owner,"video")
            videoclip = VideoClip(title=form.cleaned_data['title'],
                                  fileclip = 'media/elearning/static/video/'+str(owner)+"_" + request.FILES['fileclip'].name, 
                                 shortdetail  = form.cleaned_data['shortdetail'], 
                                 published_date = form.cleaned_data['published_date'],
                                 demo=form.cleaned_data['demo'])
            videoclip.save()    
            c = OnlineCourse.objects.get(id = courseid)
            c.videoclip.add(videoclip)
            c.save()
            return redirect("/listvideo/"+str(courseid)+"/")
        else:
           return render(request, "errorform.html", {'formerrors':form.errors})
   # if a GET (or any other method) we'll create a blank form
    else:
            
        form = VideoForm()
        
    return render(request, "createvideo.html", {"form": form})

#Use case: Manage course
def edit_videoclip(request, courseid=0,videoid=0):
    if courseid != 0:
        request.session['create_courseid'] = courseid
    else:
        courseid = request.session['create_courseid']    
     
    if request.method == "POST":
        form = VideoForm(request.POST)
        owner  = request.session['member_id']
        
        if form.is_valid():
            videoclip = VideoClip.objects.get(id = videoid)
            videoclip.title =form.cleaned_data['title']
            videoclip.shortdetail  = form.cleaned_data['shortdetail']
            videoclip.published_date = form.cleaned_data['published_date']
            videoclip.demo=form.cleaned_data['demo']
            videoclip.save()    
           
            return redirect("/listvideo/"+str(courseid)+"/")
        else:
            return render(request, "errorform.html", {'formerrors':form.errors})
 
    # if a GET (or any other method) we'll create a blank form
    else:
        videoclip = VideoClip.objects.get(id = videoid)
        form = VideoForm(instance = videoclip)
        context = Context()
        context['form'] = form
        context['courseid'] = courseid
        context['videoid'] = videoid
         
    return render(request, "editvideo.html", {"context": context})

#Use case: Manage course
def del_video(request, videoid):
    video = VideoClip.objects.get(id = videoid)
    video.delete()
    return render(request, "thanksdelvideo.html")

def admin_manage(request):
    return render(request, "adminpage.html")

from django.forms import modelformset_factory
#Use case: Approve member
def approve_fill(request):
    ApproveFormSet = modelformset_factory(Member, form = ApproveForm ,max_num=5,extra=0)
    if request.method == "POST":
        formset = ApproveFormSet(request.POST)
        if formset.is_valid():
           formset.save()
           return render(request, "thanksapprove.html")
        else:
           return render(request, "errorform.html", {"formerrors":formset.errors })
    else:
        formset = ApproveFormSet()
        
    return render(request, "approveform.html", {"formset": formset})

#Use case: Approve payment
def approve_payment(request):
    ApproveFormSet = modelformset_factory(Payment, form = CourseApproveForm ,extra=0)
    if request.method == "POST":
        formset = ApproveFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect("/paymentapprove/")
        else:
            return render(request, "errorform.html",{'formerrors': formset.errors})
    else:
        formset = ApproveFormSet()
        
    return render(request, "approvepayment.html", {"formset": formset})

#Use case: Approve course
def approve_course(request):
    
    ApproveFormSet = modelformset_factory(OnlineCourse, form = ApproveCourseForm ,extra=0)
    if request.method == "POST":
        formset = ApproveFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            
            return redirect("/approvepublish/")
        else:
            print(formset.errors)
            return render(request, "errorform.html",{'formerrors': formset.errors})
    else:
        formset = ApproveFormSet()
        
    return render(request, "approvepublish.html", {"formset": formset})

def ListMyCourse(request):
    useraccess = request.session['member_id']
    username = request.session['member_firstname']
    usersessionkey  = request.session["session_key"]
    memberacc = Member.objects.get(id = useraccess)
    mycourse = Payment.objects.filter(member = memberacc, checkpaid = True)
    listcourse =[]
    #Outer loop
    for mc in mycourse:
        #Inner loop  
        for c in OnlineCourse.objects.all():
            if c == mc.course:
                listcourse.append(c)
    return render(request, "memberpage.html", {"mycourse": listcourse})
