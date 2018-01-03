from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
)
from blog.models import PostModel


class PostModelSerializer(ModelSerializer):
    class Meta:
        model = PostModel
        fields = '__all__'


class PostModelListSerializer(ModelSerializer):
    retrieve_url = HyperlinkedIdentityField(
        view_name='blog:api:retrieve',
        lookup_field='id'
    )
    destroy_url = HyperlinkedIdentityField(
        view_name='blog:api:destroy',
        lookup_field='id'
    )

    class Meta:
        model = PostModel
        fields = ['retrieve_url', 'destroy_url']

# class PostModelListSerializer(ModelSerializer):
#     user = SerializerMethodField()
#
#     class Meta:
#         model = PostModel
#         fields = ['user']
#
#     @staticmethod
#     def get_user(obj):
#         return obj.user.username

