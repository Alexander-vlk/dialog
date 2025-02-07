from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from auth_service.serializers import UserSerializer


class RegistrationAPIView(APIView):
    """APIView для рагистрации пользователей"""
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            
            refresh.payload.update({
                'user_id': user.id,
                'username': user.username,
            })
            
            return Response(
                {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                },
                status=status.HTTP_201_CREATED,
            )
