from .serializers import UserSerializers
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from account.models import User

class UserListCreateApiView(ListCreateAPIView):
    serializer_class = UserSerializers
    permission_classes = (AllowAny,)
    queryset = User.objects.all()


    def post(self, request):
        serializers=self.serializer_class(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        status_code=status.HTTP_201_CREATED
        response={
            'success': 'True',
            'status code': status_code,
            'message': 'Пользователь успешно зарегистрированн'
        }

        return Response(response, status=status_code)