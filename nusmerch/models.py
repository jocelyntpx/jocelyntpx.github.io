from django.db import models

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

	def __str__(self):
		return self.user_name

