from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.authtoken.models import Token
from requests.serializers import RegistrationSerializer

@api_view(['POST',])
def registration_user(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Usuário registrado com sucesso."
            data['email'] = user.email
            data['nome'] = user.nome
            token = Token.objects.get(user=user).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)