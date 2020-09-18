from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000
    path('', views.index),
    # localhost:8000/savetodo/
    path('savetodo/', views.savetodo),
    # localhost:8000/about/
    path('about/', views.about),
    # localhost:8000/blog/
    path('blog/', views.blogview),
    # localhost:8000/redirect/
    path('redirect/', views.redirect),
    # localhost:8000/fruits/
    path('fruits/', views.fruits),
]