from django.http import JsonResponse
from .models import Event
from .serializers import EventSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# decorator
@api_view(['GET', 'POST'])

# formatting json 
# def event_list(request, format=None):
def event_list(request, format=None):

    if request.method == 'GET':
        #get all the Events
        events = Event.objects.all()
        #serialize them
        serializer = EventSerializer(events, many=True)
        #return json
        return Response(serializer.data)
        
    if request.method == 'POST':
        serializer = EventSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def event_detail(request, id, format=None):

    try:
        event = Event.objects.get(pk = id)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EventSerializer(event)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
