from django.conf.urls import  url,include
from app6_user import views

app_name = "app6_user"

urlpatterns = [
    url(r'^registratrion/$',views.registration,name="registration"),
    url(r'^user_login/$',views.user_login,name="user_login"),
    url(r'^index/$',views.index,name="index"),
    url(r'^user_logout/$',views.user_logout,name="user_logout"),
]
