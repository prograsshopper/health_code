import traceback

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.db import transaction
from django.views.generic import View
from django.contrib.auth import login
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from rest_framework import viewsets, mixins
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from account.models import User
from account.serializers import UserSerializer
from center.models import Center


class UsersViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = User.objects.all()
    lookup_field = 'id'
    serializer_class = UserSerializer
    pagination_class = LimitOffsetPagination

    def list(self, request):
        users = self.queryset
        page = self.paginate_queryset(users)
        return self.get_paginated_response(self.serializer_class(page, many=True).data)

    def retrieve(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=self.kwargs['id'])
        except ObjectDoesNotExist:
            raise ValidationError({'detail': 'Unknown center.'})
        return Response(self.serializer_class(user).data)
    
    def create(self, request, *args, **kwargs):
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        name = request.POST.get('name', '')
        if not email or not password or not name:
            result = {'result':'error', 'error': 'No Required Field', 'error_msg': 'Email, Password, Name은 필수입니다.'}
            return JsonResponse(result)
        phone = request.POST.get('phone', '')
        is_partner = request.POST.get('is_partner', '')
        is_partner = True if is_partner == 'true' else False
        if is_partner:
            center = request.POST.get('center', '')
            center = Center.objects.filter(id=center).first()
            if not center:
                result = {'result':'error', 'error': 'No Required Field', 'error_msg': '직원의 경우 센터 코드는 필수입니다.'}
            return JsonResponse(result)
        else:
            center = None
        nick_name = request.POST.get('nick_name', '')

        user = User.objects.filter(email=email).first()
        if user:
            result = {'result':'error', 'error': 'User Exist', 'error_msg': '동일한 이메일을 가진 유저가 존재합니다.'}
            return JsonResponse(result)
        sid = transaction.savepoint()
        try:
            with transaction.atomic():
                user = User(
                    username=email,
                    email=email,
                    phone=phone,
                    is_partner=is_partner,
                    center=center,
                    name=name,
                    nick_name=nick_name
                )   
                user.set_password(password)
                user.save()
            transaction.savepoint_commit(sid)
            result = {'result':'success', 'error':'', 'error_msg':''}
        except:
            traceback.print_exc()
            transaction.savepoint_rollback(sid)
            result = {'result':'error', 'error': 'Exception in generating User', 'error_msg': '유저 생성 과정중 예외가 발생했습니다.'}
        return JsonResponse(result)


class LoginView(View):
    @method_decorator(csrf_exempt)
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        
        if not email or password:
            result = {'result':'error', 'error': 'No Required Field', 'error_msg': 'Email, Password는 필수입니다.'}
            return JsonResponse(result)
        user = User.objects.filter(email=email).first()
        if not user:
            result = {'result':'error', 'error': 'No User', 'error_msg': '해당 유저가 존재하지 않습니다.'}
            return JsonResponse(result)
        pw_valid = user.check_password(password)
        if not pw_valid:
            result = {'result':'error', 'error': 'Invalid Password', 'error_msg': '비밀번호가 틀렸습니다.'}
            return JsonResponse(result)
        login(request, user)
        token, token_created = Token.objects.get_or_create(user=user)
        result = {'result':'success', 'error':'', 'error_msg':'', 'token': token.key}
        return JsonResponse(result)