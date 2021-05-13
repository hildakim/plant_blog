from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="o-log/home"),
    path('observation/<str:id>', detail, name="o-log/detail"),
    path('new/', new, name="o-log/new"),
    # path('create/', create, name="create"),
    path('edit/<str:id>', edit, name="o-log/edit"),
    # path('update/<str:id>', update, name="update"),
    path('delete/<str:id>', delete, name="o-log/delete"),
]