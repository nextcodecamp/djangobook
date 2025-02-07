from django.db import models

category = [
    ("EDU", "Education"),
    ("ENT", "Entertainment"),
    ("SCI", "Science fition"),
    ("SPT", "Sport"),
   
]
class Video(models.Model):
    title = models.CharField(max_length=50)
    #published_date = models.DateField()   
    published_date = models.DateField(null=True)
    category = models.CharField(choices = category, max_length=3, default = "EDU")

class Author(models.Model):
    id = models.CharField(primary_key = True, max_length=13, auto_created=False)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=10, blank=True)
    joined_date = models.DateField()
    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    #Model method การสร้างเมท็อดให้กับโมเดล เพื่อเรียกชื่อและนามสกุล 
    def full_name(self):
        "Returns the person's full name."
        return  f"{self.firstname} {self.lastname}"
    def threedigits(self):
        "Returns first three digits of phone."
        threedigit = self.phone[0:3]
        return f"{threedigit}"