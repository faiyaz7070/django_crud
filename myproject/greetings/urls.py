from django.urls import path
from . import views
urlpatterns=[
    path('',views.welcome,name="welcome"),
    path('greet/<str:username>',views.greet_user,name="greetuser"),
    path('goodbye/<str:username>',views.farewell_user,name="farewelluser")
]
