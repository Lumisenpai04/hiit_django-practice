from django.urls import path
from projectapp import views 


urlpatterns = [
    path("",views.home),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("blog", views.blog, name="blog"),
    path("service", views.service, name="service"),
    path("employees", views.employees, name="employees"),
    path("google", views.google)
]
