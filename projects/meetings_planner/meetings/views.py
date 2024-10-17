# website/views.py
from django.shortcuts import redirect, render, get_object_or_404 
from meetings.forms import MeetingForm
from .models import Meeting  # Importe le modèle de réunion si nécessaire
from .models import Room

def meetings_list_view(request):
    meetings = Meeting.objects.all()  # Récupère toutes les réunions
    return render(request, 'meetings/meetings_list.html', {'meetings': meetings})
def detail(request, id):
    meeting = get_object_or_404(Meeting, id=id)  # Correct model name and function
    return render(request, "meetings/details.html", {"meeting": meeting})
def rooms_list_view(request):
    rooms = Room.objects.all() #get all room
    return render(request, "meetings/rooms.html", {"rooms": rooms,})
def detail_room(request, id):
    room = Room.objects.get(pk=id)
    return render(request, "meetings/room_details.html", {"room": room,})


def add_meeting(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()  # Sauvegarde le meeting si le formulaire est valide
            return redirect('meetings_list_view')  # Redirige vers une liste de meetings ou une autre page après ajout
    else:
        form = MeetingForm()

    return render(request, 'meetings/new.html', {'form': form})

def delete_meeting(request, id):
    meeting = get_object_or_404(Meeting, id=id)  # Récupère la réunion par ID ou affiche une erreur 404 si elle n'existe pas
    meeting.delete()  # Supprime la réunion
    return redirect('meetings')  # Redirige vers la liste des réunions après suppression