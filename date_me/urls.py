from django.conf.urls import url
from . import views

app_name = "date_me"

urlpatterns = [
    #home
    url(r'^$', views.index, name='index'),
    
   
    #     url(r'^$',views.detail,name=''),
   
]