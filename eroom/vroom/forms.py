from django import forms

#class VideoForm(forms.Form):
#    video_title = forms.CharField(label="Video title", max_length=50)
#    video_publish = forms.DateField(label="Published date")


#Form ก้อนทำการควบคุมการป้อนข้อมูลเข้า
#class InquiryForm(forms.Form):
#    subject = forms.CharField(max_length = 100)
#    message = forms.CharField(widget=forms.Textarea)
#    sender = forms.EmailField()
#    cc_myself = forms.BooleanField(required=False)
subject_choice = (
    ("topic1", "Network"),
    ("topic2", "Software"),
    ("topic3", "Hardware"),
    ("topic4", "Others")
    )

from django.core.exceptions import ValidationError 
from django.core import validators 

#Function for validation 
def validate_sender(value):
        if len(value) < 10 :
            raise ValidationError(("%(value)s is not right. Lenght should be more than 10."),
                params={"value": value},
            )

#Form ที่มีการกำหนดการป้อนข้อมูลเข้า หน้า 63
class InquiryForm(forms.Form):
    subject = forms.ChoiceField(choices = subject_choice)
    message = forms.CharField(widget=forms.Textarea, help_text="Please give concise information.")
    #Validate by proposed function
    sender = forms.EmailField(validators=[validate_sender], help_text='Your email')
    #cc_mail = MultiEmailField()	
    cc_myself = forms.BooleanField(required=False)

#Function สำหรับการตรวจทานฟิลด์ที่กำหนดขึ้นเอง
#ในฟอร์มคือ cc_mail ซึ่งจะกำหนดแทน cc_myself
#หากต้องการดูการทำงานให้เอา cc_myself ออกแล้วกำหนด cc_mail แทน
#หน้า 72
class MultiEmailField(forms.Field):
    def to_python(self, value):
        """Normalize data to a list of strings."""
        # Return an empty list if no input was given.
        if not value:
            return []
        return value.split(",")

    def validate(self, value):
        """Check if value consists only of valid emails."""
        # Use the parent's handling of required fields, etc.
        super().validate(value)
        for email in value:
            validate_email(email)


from django.forms import ModelForm
from vroom.models import Video, Author
from django.forms import TextInput, DateInput
#Model form สำหรับใช้ในหนึ่งวิว
#ยกเลิกฟอร์มเก่าในบรรทดที่ 3-5 
from datetime import date

class VideoForm(ModelForm):
     class Meta:
        model = Video
        fields = ['title','published_date'] 
        today =  date.today()
        widgets= {
                   "published_date" : DateInput(attrs={"format":  "%Y-%m-%d", "value": today  }), }

#Model form หน้า 65 การสร้างโมเดลฟอร์ม
class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ["id","firstname", "lastname", "phone", "joined_date"]
        today =  date.today()
        widgets= {"id": TextInput(attrs={"size": 30 }),
                                                  "firstname": TextInput(attrs={"size": 30 }),
                                                  "lastname": TextInput(attrs={"size": 30 }),
                                                   "phone": TextInput(attrs={"size": 30 }),
                                                   "joined_date" : DateInput(attrs={"format":  "%Y-%m-%d", "value": today  }),
                                             
                                                  }
