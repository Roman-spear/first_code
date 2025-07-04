from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from app_modules.userapp import views

app_name = "userapp"

urlpatterns = [
    path('',views.IndexView.as_view(),name="indexview"),
]