from django.conf.urls import url, include
from app5 import views

app_name = "app5"

urlpatterns = [
    url(r'^relative/$',views.relative_url,name="relative_url"),
    url(r'^other/$',views.other,name="other"),
]
