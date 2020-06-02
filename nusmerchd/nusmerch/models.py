from django.db import models

# Create your models here.
class userInfo(models.Model):
	user_name = models.CharField(max_length=200)
	user_number = models.IntegerField(max_length=8) 
	user_email = models.CharField(max_length=200)
	faculty = models.CharField(max_length=50)
	user_password = models.CharField(max_length=50)
	user_repeatpass = models.CharField(max_length=50)

	def __str__(self):
		return self.user_name

