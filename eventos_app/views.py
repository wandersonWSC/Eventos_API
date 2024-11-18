from rest_framework import viewsets, permissions
from .models import Evento, Participante
from .serializers import EventoSerializer, ParticipanteSerializer
from django.shortcuts import render

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [permissions.IsAuthenticated]

class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        
        evento = serializer.validated_data.get('evento')
        serializer.save(evento=evento)

def home(request):
    return render(request, 'home.html')