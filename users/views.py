from rest_framework.generics import ListAPIView

from users.models import User
from users.serializers import UserSerializer


class ProfileViewset(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
