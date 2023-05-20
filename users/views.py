from rest_framework import viewsets, permissions, authentication
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import get_user_model
from . serializers import UserSerializer, AuthTokenSerializer
from . permissions import isUserOrReadOnly

# Create your views here.

class UsersView(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication,]

    def get_permissions(self):

        if self.request.method == 'GET' or self.request.method == 'POST':
            self.permission_classes = [permissions.AllowAny,]
        else:
            self.permission_classes = [permissions.IsAuthenticated, isUserOrReadOnly]
        return super(UsersView, self).get_permissions()

class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer



    