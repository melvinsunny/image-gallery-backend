from django.urls import path
from . import views

urlpatterns = [

    path('',views.ImageListView.as_view(),name='img-det-list'),

]