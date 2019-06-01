from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'center_id', 'name', 'email', 'nick_name', 'phone',
                  'is_partner', 'created_datetime', 'updated_datetime', )
