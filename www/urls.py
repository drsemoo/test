from django.contrib import admin
from django.urls import path ,include
from . import views
from .views import Tea ,TeaList

urlpatterns = [
    path('',Tea.as_view() ,name='home'),
    path('tinymce/', include('tinymce.urls')),
    path('li', TeaList.as_view(),name= 'tealist'),
]

