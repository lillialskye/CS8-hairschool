from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
#take these 3 lines
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

#take these 3 lines
from  . import serializers
from  . import models
from  . import permissions

#this class will probably be removed before project launches
class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer
#testing Api view
    def get(self, request, format=None):
        an_apiview= [
            'Get http methods-get, post, patch'
        ]
        return Response({'message':'Hello', 'an_apiview':an_apiview})
    
    def post(self, request):
            #creates a hello message with our name
            #might be removed before production
        serializer = serializers.HelloSerializer(data = request.data)
        if serializer.is_valid():
                name = serializer.data.get('name')
                message = 'Hello {0}'.format(name)
                return Response({'message':message})
        else:
                return Response(
                    serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def put(self, request, pk=None):
        #updating an object
        return Response({'method':'put'})

    def patch(self, request, pk=None):
        #only updates fields provided in the request
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        #deletes an object
        return Response({'method': 'delete'})

class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer
    #Test API Set
    #Might not need APIView
    def list(self, request):
        #Return hello message
        #might be deleted before production
        a_viewset=[
          #  'Uses actions(create, retrieve, update, partial_update)'
        ]
        return Response({'message':'Hello', 'a_viewset':a_viewset})

    def create(self, request):
        #create a new hello message
        serializer = serializers.HelloSerializer(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        #gets an object by ID
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        #handles updating an object
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    #creating and updating profiles

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.object.all()
    authentication_classes =(TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)


class LoginViewSet(viewsets.ViewSet):
    #checks email and password and returns an authtoken
    serializer_class = AuthTokenSerializer

    def create(self, request):
#uses the ObtainAuthToken API view to validate and create a token
        return ObtainAuthToken().post(request)


    