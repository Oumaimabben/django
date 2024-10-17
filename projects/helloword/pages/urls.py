from django.urls import path

from .views import home_page_view

#domain.com/pages/....
urlpatterns=[
    path('home/' ,home_page_view, name="home"),
]