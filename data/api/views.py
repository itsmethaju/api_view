from rest_framework.views import APIView
from rest_framework.response import Response, responses
from rest_framework import serializers, status
from .serializer import UserSerializer
from .models import registration
# Create your views here.

class Userview(APIView):
    def get(self,request):
        user = registration.all()
        query = self.request.GET.get('search')
        if query is not None:
            user = user.filter(name_contains = query)| user.filter(creator_contains=query)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)