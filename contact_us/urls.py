from django.urls import path
from . import views


app_name = 'contact_us'
urlpatterns = [
    path('us', views.contact_us, name='contact_us'),
]