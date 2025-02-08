from django.db import models

class UserType(models.Model):
    usertype = models.CharField(max_length=5)       
    userdetail = models.CharField(max_length=255)
    def __str__(self):
        return self.usertype
    
# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    userlogin = models.EmailField(max_length=200, blank=True)
    userpass = models.CharField(max_length=13, blank=True)
    phone = models.CharField(max_length=10)
    joined_date = models.DateField()    
    usertype = models.ForeignKey(UserType, on_delete= models.DO_NOTHING, null=True)
    def __str__(self):
        return f'{self.firstname} {self.lastname}'

class Member(User):
    expire_date = models.DateField(null=True)
    approve = models.BooleanField(default=False, blank=True)
    def check_password(self,upass):
        if (self.userpass == upass):
            return True    
        else:
            return False
    def __str__(self):
        return f'{self.firstname} {self.lastname}'

class VideoClip(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=50)
    published_date = models.DateField(null=True)
    fileclip = models.FileField(blank=True)
    shortdetail = models.CharField(max_length=300, default="")
    demo = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.title} '

class OnlineCourse(models.Model):
    id = models.BigAutoField(primary_key=True,auto_created=True)
    title = models.CharField(max_length=250, default="")
    cover = models.ImageField(blank=True)
    briefdetail = models.CharField(blank=True, max_length=500)
    saleprice = models.IntegerField(default=299)
    approve = models.BooleanField(default=False)
    owner = models.ForeignKey(Member,on_delete=models.DO_NOTHING, null=True)
    #videoclip = models.ManyToManyField(VideoClip, blank=True)
    videoclip = models.ManyToManyField(VideoClip, blank=True, related_name= "videoclips", related_query_name= "videoclip")

    published_date = models.DateField(null=True)
    def __str__(self):
        return f'{self.title} {self.id}'

class Payment(models.Model):
    pay_date = models.DateTimeField()
    member = models.ForeignKey(Member, 
                     on_delete=models.DO_NOTHING, null=True)    
    course = models.ForeignKey(OnlineCourse, 
                     on_delete=models.DO_NOTHING, null=True)    
    paidprice = models.IntegerField(default=299, blank=True)
    checkpaid = models.BooleanField(default=False)



class PaySubscription(models.Model):
    pay_date = models.DateTimeField()
    member = models.ForeignKey(Member, on_delete=models.DO_NOTHING, null=True)    
    paidprice = models.IntegerField(default=599, blank=True)
    checkpaid = models.BooleanField(default=False)


class Author(models.Model):
    id = models.CharField(primary_key = True, max_length=13, auto_created=False)
    firstname = models.CharField(max_length=55)
    lastname = models.CharField(max_length=55)
    phone = models.CharField(max_length=10)
    joined_date = models.DateField()

class CourseOwner(Author):
    def __str__(self):
        return f'{self.firstname} {self.lastname}'    
class ContactPerson(Author):

    def __str__(self):
        return f'{self.name} '    
    