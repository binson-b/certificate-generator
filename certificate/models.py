from django.db import models
from django.contrib.auth.models import User
# Create your models here.

events = (
            ('SLC', 'Scilab Conference'),
            ('SPC', 'Scipy Conference'),
            ('PTC', 'Python Textbook Companion'),
            ('STC', 'Scilab Textbook Companion'),
        )

class Profile(models.Model):
    user = models.OneToOneField(User)
    # other details
    uin = models.CharField(max_length=50)  #2 intialletters + 6 hexadigits
    attendance = models.NullBooleanField()

class Event(models.Model):
    purpose = models.CharField(max_length=25, choices=events)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    # other details

class Certificate(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50, null=True, blank=True)
    serial_no = models.CharField(max_length=50) #purpose+uin+1stletter
    counter = models.IntegerField()
    workshop = models.CharField(max_length=100, null=True, blank=True)
    paper = models.CharField(max_length=100, null=True, blank=True)
    verified = models.IntegerField(default=0)

class Scilab_participant(models.Model):
    ''' Autogenerated model file csvimport Mon Dec  1 07:46:00 2014 '''
    id = models.IntegerField(primary_key=True, null=False)
    ticket_number = models.IntegerField(default=0, null=False, blank=False)
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    ticket = models.CharField(max_length=50, null=True, blank=True)
    date = models.CharField(max_length=50, null=True, blank=True)
    order_id = models.IntegerField(default=0, null=True, blank=True)
    purpose = models.CharField(max_length=10, default='SLC')
    attendance = models.BooleanField(default=False)

    class Meta:
        managed = True

class Scilab_speaker(models.Model):
    ''' Autogenerated model file csvimport Wed Dec  3 05:36:56 2014 '''

    id = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    ticket = models.CharField(max_length=100)
    paper = models.CharField(max_length=300)
    purpose = models.CharField(max_length=10, default='SLC')
    attendance = models.BooleanField(default=False)

class Scilab_workshop(models.Model):
    ''' Autogenerated model file csvimport Wed Dec  3 06:31:59 2014 '''

    id = models.IntegerField(null=False, primary_key=True, blank=False)
    name = models.CharField(max_length=300)
    ticket_number = models.IntegerField(null=True)
    email = models.CharField(max_length=300)
    workshops = models.CharField(max_length=300)
    purpose = models.CharField(max_length=10, default='SLC')
    attendance = models.BooleanField(default=False)

class FeedBack(models.Model):
    ''' Feed back form for the event '''
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    institution = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    pin_number = models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    purpose = models.CharField(max_length=10, default='SLC')
    submitted = models.BooleanField(default=False)
    answer = models.ManyToManyField('Answer')


class Question(models.Model):
    question = models.CharField(max_length=500)
    purpose = models.CharField(max_length=10, default='SLC')

class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer = models.CharField(max_length=1000)
