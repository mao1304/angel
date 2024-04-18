from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate,logout,login 
from django.contrib.auth.decorators import login_required

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Account
from .serializer import AccountSerializer

@api_view(['POST'])
def register(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        user = Account.objects.get(email=serializer.data['email'])
        user.set_password(serializer.data['password'])
        user.save()

        return Response({ 'user': serializer.data }, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class Logout(APIView):
    def post(self, request):
        request.session.flush()
        logout(request)
        return Response({'message': 'session successfully closed '}, status=status.HTTP_200_OK)




@method_decorator(csrf_exempt, name='dispatch')
class Login(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response({'error': 'email and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(request, email=email, password=password)
        if user is None:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)

        login(request, user)  

        return Response({'user': AccountSerializer(user).data}, status=status.HTTP_200_OK)


