from django.db.models import Q
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin

from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

)

from .serializers import PostModelSerializer
from blog.models import PostModel


class PostModelCreateAPIView(CreateAPIView):
    serializer_class = PostModelSerializer
    queryset = PostModel.objects.all()
    permission_classes = [AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class PostModelListAPIView(ListAPIView):
    serializer_class = PostModelSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]
    search_fields = ['title']

    def get_queryset(self, *args, **kwargs):
        queryset_list = PostModel.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(title__icontains=query) |
                    Q(content__icontains=query)
                    ).distinct()
        return queryset_list


class PostModelRetrieveAPIView(RetrieveAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'primary_key'  # default = 'pk'


class PostModelDestroyAPIView(DestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'primary_key'  # default = 'pk'























