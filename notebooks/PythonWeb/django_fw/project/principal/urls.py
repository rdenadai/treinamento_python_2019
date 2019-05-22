from django.urls import path
from .views import index

urlpatterns = [path("home/", index, name="principal_home")]
