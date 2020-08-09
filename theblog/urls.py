
from django.urls import path, include
from . import views
from .views import PostMainPageView,PhotoModelView

urlpatterns = [
  #  path('', views.home, name="home"),

    path('', PostMainPageView.as_view(), name = "home"),
    path('gallery.html/', PhotoModelView.as_view(), name = 'gallery'),
]