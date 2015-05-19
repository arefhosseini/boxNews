from captcha.fields import CaptchaField
from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()


class Profile(models.Model):
    username = models.CharField(max_length=200)
    confirmation_code = models.CharField(max_length=32)


class Signup(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    user = models.OneToOneField(User)
    captcha = CaptchaField()

    def __str__(self):
        return u'%s %s %s %s %s' % (self.firstName, self.lastName, self.userName, self.password, self.email)


class varzeshComment(models.Model):
    username = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return u'%s %s' % (self.username, self.comment)


class gameComment(models.Model):
    username = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return u'%s %s' % (self.username, self.comment)


class musicComment(models.Model):
    username = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return u'%s %s' % (self.username, self.comment)


class movieComment(models.Model):
    username = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return u'%s %s' % (self.username, self.comment)