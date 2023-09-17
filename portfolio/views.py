from django.http import HttpResponse,request
from django.urls import reverse_lazy
from django.db import models
from django.shortcuts import render,HttpResponse
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from . import models,forms
import os
from django.template import loader
from django.forms.models import model_to_dict
from PortfolioBuilder import settings
from django.views import View

# Create your views here.
class LandingPage(View):
    def get(self,request,*args,**kwargs):
        try:
            from django.db import connection
            connection.ensure_connection()
            return HttpResponse('<script>window.location.href = "home/";</script>')
        except Exception as e:
            return render(request,'portfolio/loading_page.html',{})

def dummy_portfolio(request):
    return render(request,'portfolio/dummyPortfolio.html',{})

def viewPortfolio(request):
    home = models.Introduction.objects.filter(user=request.user).order_by('-latest')
    skills = models.Skill.objects.filter(user=request.user)
    education = models.Education.objects.filter(user=request.user)
    experience = models.Experience.objects.filter(user=request.user)
    work = models.Work.objects.filter(user=request.user)
    services = models.Services.objects.filter(user=request.user)
    reviews = models.Reviews.objects.filter(user=request.user)
    resume = models.Resume.objects.filter(user=request.user)
    accounts = models.Accounts.objects.filter(user=request.user).order_by('-latest')

    return render(request,
                  'portfolio/viewPortfolio.html',
                  {
                      'path_to_img':"/static/images/dp.png",
                      'home':home,
                      'skills':skills,
                      "education":education,
                      'experience':experience,
                      'work':work,
                      'services':services,
                      'reviews':reviews,
                      'resume':resume,
                      'accounts':accounts
                      })

class Home(ListView):
    model = models.Introduction
    template_name = "portfolio/home.html"

    # def get(self, request):
    #     if not models.Resume.objects.filter(firstIteration=True,user=self.request.user).exists():
    #         resume = models.Resume(choice='NO', user = self.request.user,firstIteration=True)
    #         resume.save()
    #         return render(request, 'portfolio/home.html', {})
    #     resume = models.Resume.objects.filter(user=self.request.user).first()
    #     return render(request, 'portfolio/home.html', {})
        

class Intro(CreateView,ListView):
    model = models.Introduction
    template_name = "portfolio/intro.html"
    form_class = forms.IntroductionForm
    context_object_name = "introduction"
    template_name = "portfolio/intro.html"
    success_url = "/intro"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.email = self.request.user.email
        return super().form_valid(form)

    def get_queryset(self):
        querySet = models.Introduction.objects.filter(user=self.request.user)
        return querySet

class IntroDelete(DeleteView):
    model = models.Introduction
    template_name = "portfolio/intro.html"
    success_url = reverse_lazy("intro")

class IntroUpdate(UpdateView):
    model = models.Introduction
    form_class = forms.IntroductionForm
    template_name = "portfolio/update.html"
    success_url = "/intro"

class Skills(CreateView,ListView):
    model = models.Skill
    form_class = forms.SkillsForm
    context_object_name = "skills"
    template_name = "portfolio/skill.html"
    success_url = "/skill"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        querySet = models.Skill.objects.filter(user=self.request.user)
        return querySet
    
class SkillDelete(DeleteView):
    model = models.Skill
    template_name = "portfolio/skill.html"
    success_url = reverse_lazy("skills")

class SkillUpdate(UpdateView):
    model = models.Skill
    form_class = forms.SkillsForm
    template_name = "portfolio/update.html"
    success_url = "/skill"

class Education(CreateView,ListView):
    model = models.Education
    form_class = forms.EducationForm
    context_object_name = "education"
    template_name = "portfolio/education.html"
    success_url = "/education"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        querySet = models.Education.objects.filter(user=self.request.user)
        return querySet
    
class EducationDelete(DeleteView):
    model = models.Education
    template_name = "portfolio/education.html"
    success_url = reverse_lazy("education")

class EducationUpdate(UpdateView):
    model = models.Education
    form_class = forms.EducationForm
    template_name = "portfolio/update.html"
    success_url = "/education"

class Experience(CreateView,ListView):
    model = models.Experience
    form_class = forms.ExperienceForm
    context_object_name = "experience"
    template_name = "portfolio/experience.html"
    success_url = "/experience"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        querySet = models.Experience.objects.filter(user=self.request.user)
        return querySet
    
class ExperienceDelete(DeleteView):
    model = models.Experience
    template_name = "portfolio/experience.html"
    success_url = reverse_lazy("experience")

class ExperienceUpdate(UpdateView):
    model = models.Experience
    form_class = forms.ExperienceForm
    template_name = "portfolio/update.html"
    success_url = "/experience"

class Project(CreateView,ListView):
    model = models.Work
    form_class = forms.ProjectForm
    context_object_name = "project"
    template_name = "portfolio/work.html"
    success_url = "/project"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        querySet = models.Work.objects.filter(user=self.request.user)
        return querySet
    
class ProjectDelete(DeleteView):
    model = models.Work
    template_name = "portfolio/work.html"
    success_url = reverse_lazy("projects")

class ProjectUpdate(UpdateView):
    model = models.Work
    form_class = forms.ProjectForm
    template_name = "portfolio/update.html"
    success_url = "/project"

class Services(CreateView,ListView):
    model = models.Services
    form_class = forms.ServiceForm
    context_object_name = "services"
    template_name = "portfolio/services.html"
    success_url = "/services"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        querySet = models.Services.objects.filter(user=self.request.user)
        return querySet
    
class ServiceDelete(DeleteView):
    model = models.Services
    template_name = "portfolio/services.html"
    success_url = reverse_lazy("services")

class ServiceUpdate(UpdateView):
    model = models.Services
    form_class = forms.ServiceForm
    template_name = "portfolio/update.html"
    success_url = "/services" 


class Reviews(CreateView,ListView):
    model = models.Reviews
    form_class = forms.ServiceForm
    context_object_name = "reviews"
    template_name = "portfolio/reviews.html"
    success_url = "/reviews"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        querySet = models.Reviews.objects.filter(user=self.request.user)
        return querySet
    
class ReviewDelete(DeleteView):
    model = models.Reviews
    template_name = "portfolio/reviews.html"
    success_url = reverse_lazy("reviews")

class ReviewUpdate(UpdateView):
    model = models.Reviews
    form_class = forms.ReviewForm
    template_name = "portfolio/resume.html"
    success_url = "/reviews"

class Accounts(CreateView,ListView):
    model = models.Accounts
    form_class = forms.AccountsForm
    context_object_name = "accounts"
    template_name = "portfolio/accounts.html"
    success_url = "/accounts"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        querySet = models.Accounts.objects.filter(user=self.request.user)
        return querySet
    
class AccountsDelete(DeleteView):
    model = models.Accounts
    template_name = "portfolio/accounts.html"
    success_url = reverse_lazy("accounts")

class AccountsUpdate(UpdateView):
    model = models.Accounts
    form_class = forms.AccountsForm
    template_name = "portfolio/update.html"
    success_url = "/accounts"
    
class Resume(ListView):
    model = models.Resume
    context_object_name = "resume"
    template_name = "portfolio/resume.html"

class Download(ListView):
    model = models.Introduction
    template_name = "portfolio/guide.html"

def download_template_with_content(request):
    # Get data from the models (this can be your dynamic data)
    intro_data = models.Introduction.objects.filter(user=request.user).order_by('-latest')
    skill_data = models.Skill.objects.filter(user=request.user)
    education_data = models.Education.objects.filter(user=request.user)
    experience_data = models.Experience.objects.filter(user=request.user)
    work_data = models.Work.objects.filter(user=request.user)
    services_data = models.Services.objects.filter(user=request.user)
    reviews_data = models.Reviews.objects.filter(user=request.user)
    resume_data = models.Resume.objects.filter(user=request.user)


    # Load the template using the template loader
    template_file_path = os.path.join(settings.BASE_DIR,'templates','portfolio','viewPortfolio.html')
    template = loader.get_template(template_file_path)

    # Create a list to store the dictionaries representing the model data
    intro_data_dicts = [model_to_dict(instance) for instance in intro_data]
    skill_data_dicts = [model_to_dict(instance) for instance in skill_data]
    education_data_dicts = [model_to_dict(instance) for instance in education_data]
    experience_data_dicts = [model_to_dict(instance) for instance in experience_data]
    work_data_dicts = [model_to_dict(instance) for instance in work_data]
    services_data_dicts = [model_to_dict(instance) for instance in services_data]
    reviews_data_dicts = [model_to_dict(instance) for instance in reviews_data]
    # resume_data_dicts = [model_to_dict(instance) for instance in resume_data]


    # Render the template with the dynamic data
    rendered_content = template.render({
        'path_to_img':"dp.png",
        'home': intro_data_dicts, 
        'skills':skill_data_dicts,
        'education':education_data_dicts,
        'experience':experience_data_dicts,
        'work':work_data_dicts,
        'services':services_data_dicts,
        'reviews':reviews_data_dicts,
        # 'resume':resume_data_dicts
        })

    # Set the Content-Disposition header to prompt the user to download the file
    response = HttpResponse(rendered_content, content_type='text/html')
    response['Content-Disposition'] = 'attachment; filename="index.html"'
    return response