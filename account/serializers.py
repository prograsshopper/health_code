from rest_framework import serializers

from .models import User, Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'center_id', 'name', 'email', 'nick_name', 'phone',
                  'is_partner', 'created_datetime', 'updated_datetime', )


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'center_id', 'membership', 'title', 'content', 'point',
                  'hidden', 'created_datetime', 'updated_datetime',)
