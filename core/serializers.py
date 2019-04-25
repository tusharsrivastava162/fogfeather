from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile
from .utils import serfed


class UserSerializer(serializers.ModelSerializer):
    """
    exclude :param
    list of fields which need to be excluded during serialization
    fields :param
    '__all__' :default
    list of fields which need to be included during serialization
    """
    def __init__(self, *args, **kwargs):
        serfed(self.Meta, **kwargs)
        super(UserSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = User


class ProfileSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        serfed(self.Meta, **kwargs)
        super(ProfileSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Profile
