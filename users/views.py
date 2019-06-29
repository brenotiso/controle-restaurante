from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    permission_classes
)
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
import requests


CLIENT_ID = 'P5wsgBfEUXP5GscpZyCZv7H20kZPoiImm2WWyt8n'
CLIENT_SECRET = 'NzZSh0Gs0vadu2ilvbmE8p1RZgdSRumDkiIPLxFarcDADXq29eBZV95HTRD2Y6E6MrBXAQgKccJDg1ltB1U78F34JnGfj4gA7QMzRJNyKvfvpE7v4bwaXa4wMjQto67k'


@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    '''
    Gets tokens with username and password. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    '''
    r = requests.post(
        'http://localhost:8000/auth/token/',
        data={
            'grant_type': 'password',
            'username': request.data['username'],
            'password': request.data['password'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())



@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    '''
    Method to refresh tokens.
    {"refresh_token": "<token>"}
    '''
    r = requests.post(
        'http://localhost:8000/auth/token/',
        data={
            'grant_type': 'refresh_token',
            'refresh_token': request.data['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    '''
    Method to revoke tokens.
    {"token": "<token>"}
    '''
    r = requests.post(
        'http://localhost:8000/auth/revoke_token/',
        data={
            'token': request.data['token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    # If it goes well return sucess message (would be empty otherwise)
    if r.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, r.status_code)
    # Return the error if it goes badly
    return Response(r.json(), r.status_code)
