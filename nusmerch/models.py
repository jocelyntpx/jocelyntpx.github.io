from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(faculty='fass')

# Create your models here.
class userInfo(models.Model):
	faculty_types = (
		('fass','Arts and Social Sciences'),
		('biz','Business'),
		('com','Computing'),
		('den','Dentistry'),
		('sde','Design and Environment'),
		('eng','Engineering'),
		('law','Law'),
		('med','Medicine'),
		('sci','Science'),
		)
	user_name = models.CharField(max_length=200)
	user_number = models.IntegerField() 
	user_email = models.CharField(max_length=200)
	faculty = models.CharField(max_length=50,choices=faculty_types,default='fass')
	user_password = models.CharField(max_length=50)
	user_repeatpass = models.CharField(max_length=50)
	image = models.ImageField(upload_to='profile_image', blank=True)

	def __str__(self):
		return self.user_name

