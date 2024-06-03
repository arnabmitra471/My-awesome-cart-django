from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("contact/",views.contact_us,name="contact"),
    path("signup/",views.signup,name="signup"),
    path("login/",views.login,name="login")
]
