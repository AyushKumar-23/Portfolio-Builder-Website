from django.db import models
from userapp.models import CustomUser

# Create your models here.
class Introduction(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=128)
    jobRole = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    phoneNo = models.CharField(max_length=13)
    shortSummary = models.TextField()
    latest = models.DateTimeField(auto_now_add=True,editable=False)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Introduction'
        verbose_name_plural = "Introductions"

    def __str__(self):
        return self.name

class Skill(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    skill = models.CharField(max_length=30)
    expertise = models.PositiveIntegerField(default=0)

class Education(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    universityName = models.CharField(max_length=256)
    branch = models.CharField(max_length=50)
    percentage = models.IntegerField(default=0)
    startYear = models.CharField(max_length=4,default="XXXX")
    endYear = models.CharField(max_length=4,default="XXXX")

class Experience(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    companyName = models.CharField(max_length=256)
    jobRole = models.CharField(max_length=50)
    startYear = models.CharField(max_length=4,default="XXXX")
    endYear = models.CharField(max_length=4,default="XXXX")
    githubRepo = models.URLField(blank=True,null=True)

class Work(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    projectName = models.CharField(max_length=50)
    githubRepo = models.URLField(blank=True,null=True)
    description = models.TextField()

class Services(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    serviceName = models.CharField(max_length=127)
    description = models.TextField()

class Reviews(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    stars = models.IntegerField(default=0)
    review = models.TextField()
    reviewerName = models.CharField(max_length=50)
    platform = models.CharField(max_length=20)

class Resume(models.Model):
    CHOICES = (
        ('YES', 'YES'),
        ('NO', 'NO')
    )

    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    choice = models.CharField(max_length=3, choices=CHOICES, default='NO')
    firstIteration = models.BooleanField(default=False)

class Accounts(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    linkdin = models.URLField(blank=True,null=True)
    github = models.URLField(blank=True,null=True)
    codechef = models.URLField(blank=True,null=True)
    leetcode = models.URLField(blank=True,null=True)
    hackerrank = models.URLField(blank=True,null=True)
    latest = models.DateTimeField(auto_now_add=True,editable=False)
