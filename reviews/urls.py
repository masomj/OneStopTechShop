from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('<product_id>', views.leave_a_review, name='review'),

    ]