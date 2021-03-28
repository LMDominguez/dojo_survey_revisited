from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process', views.process),
    path('submit_page', views.submit_page)
    # path('<url>', views.catch_all)
]
