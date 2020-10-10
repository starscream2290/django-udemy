from django.conf.urls import  url
from app4 import views

app_name = "app4"

urlpatterns=[
    url(r"^index/",views.index,name="home"),
    url(r"^formpage/",views.User_form_views,name="User_form_views"),
]
