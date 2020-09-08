from rest_framework import viewsets, status
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User  # to get the current user (by pk)
from rest_framework.permissions import IsAuthenticated, AllowAny


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # what set of records in the db to use
    serializer_class = UserSerializer

    permission_classes_by_action = {'create': [AllowAny],
                                    'list': [IsAuthenticated]}

    def create(self, request, *args, **kwargs):
        return super(UserViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(UserViewSet, self).list(request, *args, **kwargs)


    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

@api_view(('GET',))
def current_user(request):
    username = str(request.user)
    return Response({"username":username})
