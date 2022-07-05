from django.urls import path
from . import views

#url to draw funtion, send image and dots to this endpoint
#localhost:8000/api/draw/
urlpatterns = [
    path("draw/", views.SplineDrawer.as_view()),
]