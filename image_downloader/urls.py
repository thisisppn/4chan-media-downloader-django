from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^download_thread_images/', views.download_thread_images)
]
