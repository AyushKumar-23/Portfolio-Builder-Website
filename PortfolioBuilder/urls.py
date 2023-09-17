from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('portfolio.urls')),
    path("user/",include("userapp.urls")),
    path("user/",include("django.contrib.auth.urls")),
]