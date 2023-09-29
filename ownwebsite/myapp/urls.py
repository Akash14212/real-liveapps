from django.urls import path 
from . import views 
 
urlpatterns=[ 
    path('home/',views.home), 
    path('about/',views.about), 
    path('courses/',views.courses), 
    path('edunet/',views.edunet),
]