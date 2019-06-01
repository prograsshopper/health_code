from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Center, Membership, CenterCategory, Program
from .serializers import (
    CenterSerializer, CenterCategorySerializer, ProgramSerializer, MembershipSerializer
)


class CenterViewSet(viewsets.GenericViewSet, ):
    lookup_field = 'id'
    serializer_class = CenterSerializer
    pagination_class = LimitOffsetPagination
    queryset = Center.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )

    def list(self, request):
        centers = self.queryset
        page = self.paginate_queryset(centers)
        return self.get_paginated_response(self.serializer_class(page, many=True).data)

    def retrieve(self, request, *args, **kwargs):
        try:
            center = Center.objects.get(id=self.kwargs['id'])
        except ObjectDoesNotExist:
            raise ValidationError({'detail': 'Unknown center.'})
        return Response(self.serializer_class(center).data)

    @action(methods=['get'], detail=True)
    def members(self, request, *args, **kwargs):
        users = Membership.objects.filter(center_id=self.kwargs['id']).all()
        page = self.paginate_queryset(users)
        return self.get_paginated_response(CenterSerializer(page, many=True).data)

    @action(methods=['get'], detail=True)
    def programs(self, request, *args, **kwargs):
        programs = Program.objects.filter(center_id=self.kwargs['id']).all()
        page = self.paginate_queryset(programs)
        return self.get_paginated_response(ProgramSerializer(page, many=True).data)


class CenterCategoryViewSet(viewsets.GenericViewSet):
    lookup_field = 'id'
    serializer_class = CenterCategorySerializer
    pagination_class = LimitOffsetPagination
    queryset = CenterCategory.objects.all()

    def list(self, request):
        categories = self.queryset
        page = self.paginate_queryset(categories)
        return self.get_paginated_response(self.serializer_class(page, many=True).data)

    def retrieve(self, request, *args, **kwargs):
        try:
            category = CenterCategory.objects.get(id=self.kwargs['id'])
        except ObjectDoesNotExist:
            raise ValidationError({'detail': 'Unknown Category.'})
        return Response(self.serializer_class(category).data)


class ProgramViewSet(viewsets.GenericViewSet):
    lookup_field = 'id'
    serializer_class = ProgramSerializer
    pagination_class = LimitOffsetPagination
    queryset = Program.objects.all()

    def retrieve(self, request, *args, **kwargs):
        try:
            program = Program.objects.get(id=self.kwargs['id'])
        except ObjectDoesNotExist:
            raise ValidationError({'detail': 'Unknown Program.'})
        return Response(self.serializer_class(program).data)

    @action(methods=['get'], detail=True)
    def memberships(self, request, *args, **kwargs):
        memberships = Membership.objects.filter(program_id=self.kwargs['id']).all()
        page = self.paginate_queryset(memberships)
        return self.get_paginated_response(MembershipSerializer(page, many=True).data)


class MembershipViewSet(viewsets.GenericViewSet):
    lookup_field = 'id'
    serializer_class = MembershipSerializer
    pagination_class = LimitOffsetPagination
    queryset = Membership.objects.all()

    def retrieve(self, request, *args, **kwargs):
        try:
            membership = Membership.objects.get(id=self.kwargs['id'])
        except ObjectDoesNotExist:
            ValidationError({'detail': 'Unknown Membership'})
        return Response(self.serializer_class(membership).data)
