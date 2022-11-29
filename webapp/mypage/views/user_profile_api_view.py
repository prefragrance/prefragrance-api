from accounts.models import User
from accounts.serializers import UserProfileSerializer
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class UserProfileAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(
            {"user_profile": serializer.data, "medal": "temp"},
            status=status.HTTP_200_OK,
        )
