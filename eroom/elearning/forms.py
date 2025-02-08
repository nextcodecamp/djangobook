from django.forms import ModelForm # type: ignore
from elearning.models import PaySubscription, OnlineCourse,ContactPerson,VideoClip, CourseOwner, Member, Payment
from django.forms.widgets import TextInput, PasswordInput, DateInput, DateTimeInput, NumberInput,Select,ClearableFileInput, Textarea # type: ignore
from django.forms import FileField
from datetime import date
from django import forms
from django.conf import settings 

class RegisterForm(ModelForm):
    class Meta:
        model = Member
        fields = ["firstname", "lastname", "userlogin", "userpass", "phone" ]
        widgets = {
            'firstname': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'your firstname'
                }),
            'lastname': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'your last name'
                }),
             'userlogin': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'your user login, length less than 13.'
                }),
            'userpass': PasswordInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'your user login, length less than 13.'
                }),
                'phone': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
              
                'placeholder': 'Phone number'
                }),
             
                
                 
                
        }
from datetime import date, timedelta,datetime


class CourseForm(ModelForm):
    class Meta:
        
        model = OnlineCourse
        
        fields = ["title",  "cover", "briefdetail", "saleprice"]
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
              
                }),
                'cover': ClearableFileInput(attrs={
                   
                }),
               'briefdetail': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
              
                }),
                

                }
    
class ApproveForm(ModelForm):
    class Meta:
        model = Member
        fields = ["firstname", "lastname", "joined_date", "phone", "approve", "expire_date" ]
        widgets = {
            'firstname': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'your firstname'
                }),
            'lastname': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'your last name'
                }),
            
                'phone': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Phone number'
                }),
                 'expire_date': DateInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Phone number'
                }),
            
                
        }




class CourseForm(ModelForm):
    class Meta:
        
        model = OnlineCourse
        
        fields = ["title",  "cover", "briefdetail", "saleprice"]
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
              
                }),
                'cover': ClearableFileInput(attrs={
                   
                }),
               'briefdetail': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
              
                }),
                

                }
#For approve course

class ApproveCourseForm(ModelForm):
    class Meta:
        
        model = OnlineCourse
        
        fields = ["title",  "cover", "briefdetail", "saleprice", "approve"]
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
              
                }),
                'cover': ClearableFileInput(attrs={
                  
                }),
               'briefdetail': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
              
                }),
                

                }

#For approve payment        
class CourseApproveForm(ModelForm):
    class Meta:
        model = Payment
        fields = ["course", "member", "paidprice", "pay_date", "checkpaid" ]
        widgets = {
            'course': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
               # 'disabled': True
                }),
            'member': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
               # 'disabled': True
                }),
            
            'pay_date': DateTimeInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
               # 'disabled': True
                }),
            'paidprice': NumberInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
               # 'disabled': True
                }),


       
                
                }
        
from django import forms # type: ignore

from django.core.exceptions import ValidationError # type: ignore
#from django.core import validators # type: ignore
from django.core.validators import validate_email, EmailValidator

def validate_subject(value):
        if len(value) < 10 :
            raise ValidationError(("%(value)s is not right. Length should be more than 10."),
                params={"value": value},
            )
class InquiryForm(forms.Form):
    sender = forms.EmailField(validators=[EmailValidator(message="Invalid email address. Please check again") ]) # type: ignore
    subject = forms.CharField( max_length=255, validators=[validate_subject])
    message = forms.CharField(widget=forms.Textarea)
    def clean_message(self):
        message = self.cleaned_data.get['message']
        if len(message) > 100:
           raise ValidationError(("%(value)s is not right. Length should not be more than 100 characters."),
                params={"value": value},
            )
 
        

class LoginForm(forms.Form):
    
    loginuser = forms.EmailField(validators=[EmailValidator(message="Invalid email address. Please check again") ]) # type: ignore
    loginpass = forms.CharField(widget=forms.PasswordInput())

from django.core.exceptions import ValidationError 
from django.utils.translation import gettext_lazy as _ 
def validate_even(value): 
	if value % 2 != 0: raise ValidationError( _("%(value)s is not an even number, raised by form"), params={"value": value}, )

class Subscription(ModelForm):
    class Meta:
        model = PaySubscription
        fields = ["pay_date","member","paidprice" ]
       
class Profile(ModelForm):
    class Meta:
        model = Member
        fields = ["firstname", "lastname", "userlogin", "userpass","phone","joined_date","expire_date" ]
        widgets = {
              'userpass': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),
                'firstname': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),
                'lastname': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),

              'userlogin': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'disabled': True
                }),

        'expire_date': DateTimeInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
               # 'disabled': True
                }),
                  'joined_date': DateTimeInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
               # 'disabled': True
                }),
        }
