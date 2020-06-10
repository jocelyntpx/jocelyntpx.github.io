from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


from django.utils.translation import gettext_lazy as _
from datetime import date
from django.dispatch import receiver

class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(faculty='fass')

# Create your models here.
class userInfo(models.Model):
	faculty_types = [
	('FASS','Arts and Social Sciences'),
	('BIZ','Business'),
	('COM','Computing'),
	('DEN','Dentistry'),
	('SDE','Design and Environment'),
	('ENG','Engineering'),
	('LAW','Law'),
	('MED','Medicine'),
	('SCI','Science'),
	]

	Campus_Residential = [
    ('TH', 'Temasek Hall'),
    ('EH', 'Eusoff Hall'),
   	('SH', 'Sheares Hall'),
   	('RH', 'Raffles Hall'),
   	('KR', 'Kent Ridge Hall'),
   	('TEM', 'Tembusu'),    	
   	('RVRC', 'Ridge View Residences'),
	('CAPT', 'College of Alice and Peter Tan'),
    ('USP', 'University Scholars Programme'),
    ('RC4', 'Residential COllege 4'),
    ('NIL', 'Do Not Stay On Campus'),
    ]
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField('Full Name',max_length=200)
	number = models.IntegerField()
	matric = models.CharField('Matric Number',max_length=10,help_text='AXXXXXXXB') 
	email = models.EmailField(max_length=200, blank=False)
	faculty = models.CharField(
    	max_length=50,
    	choices=faculty_types,
    	default='FASS')
	campus_residential_type = models.CharField('Campus Residential Type',
    max_length=100, choices=Campus_Residential,
    default='NIL')
	password1 = models.CharField(max_length=50)
	password2 = models.CharField(max_length=50)
	image = models.ImageField(upload_to='profile_image', blank=True)

	def str(self):
		return f'{self.user.username} Profile'
