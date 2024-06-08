from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path('list', views.listtweet, name="listtweet"), #tanersuzen.com/tweetapp/list
    path('add', views.addtweet, name="addtweet"), #tanersuzen.com/tweetapp/add
    path('addtweetbyform',views.addtweetbyform, name="addtweetbyform") #tanersuzen.com/tweetapp/addtweetbyform
]