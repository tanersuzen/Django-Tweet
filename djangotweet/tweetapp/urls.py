from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path('tweets', views.listtweet, name="listtweet"), #tanersuzen.com/tweetapp/tweets
    path('add', views.addtweet, name="addtweet"), #tanersuzen.com/tweetapp/add
    path('addtweetbyform',views.addtweetbyform, name="addtweetbyform"), #tanersuzen.com/tweetapp/addtweetbyform
    path('addtweetbymodelform',views.addtweetbymodelform, name="addtweetbymodelform"), #tanersuzen.com/tweetapp/addtweetbymodelform
    path('',views.base, name="base"), #tanersuzen.com/
    path('signup',views.SignUpView.as_view(), name="signup"),
    path('deletetweet/<int:id>',views.deletetweet, name="deletetweet")
]