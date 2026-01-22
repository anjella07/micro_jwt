from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import UserProfile
from .serializers import UserProfileSerializer
from .filter import UserProfileFilter
from .pagination import StandardResultsSetPagination


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = UserProfileFilter
    search_fields = ['first_name', 'last_name', 'phone_number']
    ordering_fields = ['age', 'date_registered', 'status']
    ordering = ['date_registered']
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]

class PublicViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]