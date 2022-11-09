from django.http import JsonResponse
from .models import Event
from .serializers import EventSerializer

def event_list(request):

    #get all the Events
    events = Event.objects.all()
    #serialize them
    serializer = EventSerializer(events, many=True)
    #return json
    # return JsonResponse(serializer.data, safe=False)
    return JsonResponse({'events': serializer.data}, safe=False)