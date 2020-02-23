from django.db import models

from django.urls import reverse

# Create your models here.

class User(models.Model):
    userid = models.CharField(max_length = 20, unique=True, primary_key=True)
    userpw = models.CharField(max_length = 30)
    userSchool = models.CharField(max_length = 50, default='서울여자대학교')
    userHakbun = models.CharField(max_length = 20, default='')
    userEmail = models.CharField(max_length = 50, default='')
    userName = models.CharField(max_length = 30, default='')

    def __str__(self):
        return self.userid

class UserLecture(models.Model):

    RATING_FIELD = (
        ('on', 'on'),
        ('off', 'off'),
    )

    myuserid = models.ForeignKey('User', on_delete=models.CASCADE, to_field='userid', related_name='myuserid', primary_key=True, unique=True)
    mylectureid = models.ForeignKey('Lecture', to_field='lectureid',on_delete=models.CASCADE, related_name='mylectureid')
    rating = models.CharField(max_length=10, choices=RATING_FIELD, default = "off")


class Lecture(models.Model):
    semester = models.CharField(max_length = 30)
    lectureid = models.CharField(max_length=20, primary_key=True, unique=True)
    lecturename = models.CharField(max_length=50)
    professor = models.CharField(max_length=50)
    
    def get_absolute_url(self):
        return reverse('detail', args=[self.lectureid])



class Board(models.Model):
    content = models.TextField()
    quality = models.IntegerField()
    challenge = models.IntegerField()
    recommend = models.IntegerField()
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='user_id')
    lecture = models.ForeignKey('Lecture', on_delete=models.CASCADE, related_name='lecture')

    def get_absolute_url(self):
        return reverse('detail', args=[self.lecture.lectureid])