from django.urls import path
from . import views

urlpatterns = [
    #path("", views.view1, name='view1'),
    path("", views.tempview, name="temp"),
    path("chi/",views.chiview, name="chi"),
    path("test/", views.PostListView.as_view(), name="list"),
]