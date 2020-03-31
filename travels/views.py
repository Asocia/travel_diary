from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from .serializers import TravelSerializer, UserSerializer
from .models import Travel
from .permissions import IsOwnerOrReadOnly

# Create your views here.

# User.objects.create_superuser(username="sahin", password="asdf1234")
# sample_users = [{"username": "kartaca", "password": "krtc4321"},
#                 {"username": "new_user", "password": "fdsa4321"},
#                 {"username": "something", "password": "fdsa4321"}]
#
# for user in sample_users:
#     u = User.objects.create_user(**user)
#     u.save()


class TravelViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
