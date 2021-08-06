from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.

class user(models.Model):  
    objects = models.Manager()
    id = models.AutoField(primary_key=True)  # id
    name = models.CharField(max_length=100, null=True)  # name
    password = models.CharField(max_length=100, null=True)  # password
    email = models.CharField(max_length=100, null=True)  # password


class meda(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)  # id
    rank = models.CharField(max_length=100, null=True)
    countryname = models.CharField(max_length=100, null=True)
    gold = models.CharField(max_length=100, null=True)
    silver = models.CharField(max_length=100, null=True)
    bronze = models.CharField(max_length=100, null=True)
    count = models.CharField(max_length=100, null=True)


class Sport(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    info = models.CharField(max_length=1024, null=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    pic_url = models.CharField(max_length=128, null=True)
    web_url = models.URLField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Sport, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Sports'

    def __str__(self):
        return self.name

class Athlete(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    info = models.CharField(max_length=1024, null=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Athlete, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Athletes'

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


