from rest_framework import viewsets
from . import models,serializers
from django_filters.rest_framework import DjangoFilterBackend
from . import filters

# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_class = filters.EventFilter
    
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            serializer.save()
