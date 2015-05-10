from django.db import models


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()


class Signup(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    userName = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return u'%s %s %s %s %s' % (self.firstName, self.lastName, self.userName, self.password, self.email)
