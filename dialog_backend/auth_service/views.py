from rest_framework.authentication import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from auth_service.serializers import UserSerializer


class RegistrationAPIView(APIView):
    """APIView для рагистрации пользователей"""
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
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


class LoginAPIView(APIView):
    """APIView для аутентификации пользователя"""
    
    def post(self, request):
        data = request.data
        
        username = data.get('username', None)
        password = data.get('password', None)
        
        if not username or not password:
            return Response(
                {
                    'error': 'Оба поля должны быть заполнены',
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        user = authenticate(username=username, password=password)
        
        if not user:
            return Response(
                {
                    'error': 'Неверные имя пользователя или пароль',
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
            
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
            status=status.HTTP_200_OK,
        )


class LogoutAPIView(APIView):
    """APIView для выхода пользователя"""
    
    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        
        if not refresh_token:
            return Response(
                {
                    'error': 'Необходим refresh токен',
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as invalid_token:
            return Response(
                {
                    'error': 'Некорректный refresh токен',
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        return Response(
            {
                'success': 'Выход успешно совершен',
            },
            status=status.HTTP_200_OK,
        )
