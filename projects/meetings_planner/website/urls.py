from django.urls import path
from meetings.views import meetings_list_view, detail  # Importez les vues nécessaires
from . import views

# domain.com/website/...
urlpatterns = [
    path('', views.home_view, name='home'),
    path('about', views.about_view, name='about'),
    
]
