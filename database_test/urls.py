from database_test import views
from django.urls import path


urlpatterns = [ path('db_commands/<str:name>', views.db_commands, name="db_commands") ]