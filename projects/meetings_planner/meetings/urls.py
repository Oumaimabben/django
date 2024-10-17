from . import views
from django.urls import path
from meetings.views import detail,detail_room

urlpatterns = [
    path('meetings', views.meetings_list_view, name='meetings_list_view'),  # List of meetings  
    path('detail/<int:id>/', detail, name='detail'),  # Meeting
    path('rooms' ,views.rooms_list_view ,name='rooms_list_view'),
    path('detail_room/<int:id>/', detail_room, name='detail_room'), #meeting details
    path('add-room/', views.add_meeting, name='add_meeting'),  # Chemin pour ajouter une réunion
    path('delete/<int:id>/', views.delete_meeting, name='delete'),  # Chemin pour supprimer une réunion
]
