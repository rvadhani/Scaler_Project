from django.urls import path

from tryHello import views

#name value is  help to do reverse engineering
urlpatterns = [path('hello/<str:name>', views.hello_world, name="hello world")]
