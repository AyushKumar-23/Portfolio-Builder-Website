from django import forms
from . import models

class IntroductionForm(forms.ModelForm):
    class Meta:
        model = models.Introduction
        fields = ['name','jobRole','location','phoneNo','shortSummary']

class SkillsForm(forms.ModelForm):
    class Meta:
        model = models.Skill
        fields = ["skill","expertise"]

class EducationForm(forms.ModelForm):
    class Meta:
        model = models.Education
        fields = ["universityName","branch","percentage","startYear","endYear"]

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = models.Experience
        fields = ["companyName","jobRole","githubRepo","startYear","endYear"]

class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Work
        fields = ["projectName","githubRepo","description"]

class ServiceForm(forms.ModelForm):
    class Meta:
        model = models.Services
        fields = ["serviceName","description"]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Reviews
        fields = ["stars","review","reviewerName","platform"]

class ResumeForm(forms.ModelForm):
    class Meta:
        model = models.Resume
        fields = ['choice']

class AccountsForm(forms.ModelForm):
    class Meta:
        model = models.Accounts
        fields = ['linkdin','github','codechef','leetcode','hackerrank']