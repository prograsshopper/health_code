from rest_framework import serializers

from .models import CenterCategory, Center, Program, Membership


class CenterCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CenterCategory
        fields = ('id', 'name', 'created_datetime', 'updated_datetime')


class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = ('id', 'name', 'category', 'phone', 'address', 'longitude', 'latitude', 'is_active', 'description',
                  'created_datetime', 'updated_datetime')


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ('id', 'center', 'name', 'quota', 'price', 'available', 'program_schedule', 'description',
                  'is_active', 'created_datetime', 'updated_datetime')


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ('id', 'user_id', 'center_id', 'program_id', 'start_date', 'end_date',
                  'created_datetime', 'updated_datetime')
