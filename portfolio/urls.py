from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # path('',login_required(views.Home.as_view(),login_url='/user/login/?next=/user/login/'),name='home'),
    
    path('intro/',login_required(views.Intro.as_view(),login_url='/user/login/?next=/user/login/'),name='intro'),
    path('intro/<int:pk>/delete',login_required(views.IntroDelete.as_view(),login_url='/user/login/?next=/user/login/'),name='introDelete'),
    path('intro/<int:pk>',login_required(views.IntroUpdate.as_view(),login_url='/user/login/?next=/user/login/'),name='introUpdate'),

   
    path('skill/',login_required(views.Skills.as_view(),login_url='/user/login/?next=/user/login/'),name='skills'),
    path('skill/<int:pk>/delete',login_required(views.SkillDelete.as_view(),login_url='/user/login/?next=/user/login/'),name='skillDelete'),
    path('skill/<int:pk>',login_required(views.SkillUpdate.as_view(),login_url='/user/login/?next=/user/login/'),name='skillUpdate'),


    path('education/',login_required(views.Education.as_view(),login_url='/user/login/?next=/user/login/'),name='education'),
    path('education/<int:pk>/delete',login_required(views.EducationDelete.as_view(),login_url='/user/login/?next=/user/login/'),name='educationDelete'),
    path('education/<int:pk>',login_required(views.EducationUpdate.as_view(),login_url='/user/login/?next=/user/login/'),name='educationUpdate'),

    
    path('experience/',login_required(views.Experience.as_view(),login_url='/user/login/?next=/user/login/'),name='experience'),
    path('experience/<int:pk>/delete',login_required(views.ExperienceDelete.as_view(),login_url='/user/login/?next=/user/login/'),name='experienceDelete'),
    path('experience/<int:pk>',login_required(views.ExperienceUpdate.as_view(),login_url='/user/login/?next=/user/login/'),name='experienceUpdate'),

    
    path('project/',login_required(views.Project.as_view(),login_url='/user/login/?next=/user/login/'),name='projects'),
    path('project/<int:pk>/delete',login_required(views.ProjectDelete.as_view(),login_url='/user/login/?next=/user/login/'),name='projectDelete'),
    path('project/<int:pk>',login_required(views.ProjectUpdate.as_view(),login_url='/user/login/?next=/user/login/'),name='projectUpdate'),

    
    path('services/',login_required(views.Services.as_view(),login_url='/user/login/?next=/user/login/'),name='services'),
    path('services/<int:pk>/delete',login_required(views.ServiceDelete.as_view(),login_url='/user/login/?next=/user/login/'),name='servicesDelete'),
    path('services/<int:pk>',login_required(views.ServiceUpdate.as_view(),login_url='/user/login/?next=/user/login/'),name='servicesUpdate'),

    
    path('reviews/',login_required(views.Reviews.as_view(),login_url='/user/login/?next=/user/login/'),name='reviews'),
    path('reviews/<int:pk>/delete',login_required(views.ReviewDelete.as_view(),login_url='/user/login/?next=/user/login/'),name='reviewDelete'),
    path('reviews/<int:pk>',login_required(views.ReviewUpdate.as_view(),login_url='/user/login/?next=/user/login/'),name='reviewUpdate'),

    path('accounts/',login_required(views.Accounts.as_view(),login_url='/user/login/?next=/user/login/'),name='accounts'),
    path('accounts/<int:pk>/delete',login_required(views.AccountsDelete.as_view(),login_url='/user/login/?next=/user/login/'),name='accountsDelete'),
    path('accounts/<int:pk>',login_required(views.AccountsUpdate.as_view(),login_url='/user/login/?next=/user/login/'),name='accountsUpdate'),

    path('resume/',login_required(views.Resume.as_view(),login_url='/user/login/?next=/user/login/'),name='resume'),

    path('download/',login_required(views.Download.as_view(),login_url='/user/login/?next=/user/login/'),name='download'),

    path('viewPortfolio/',login_required(views.viewPortfolio,login_url='/user/login/?next=/user/login/'),name='viewPortfolio'),
    path('download',views.download_template_with_content,name='downloadPortfolio'),

    path('dummy_portfolio/',views.dummy_portfolio,name="dummy_portfolio"),
    path('home/',views.Home.as_view(),name='home'),
    path('',views.LandingPage.as_view(),name="landing_page")
]