import traceback

from django.http import JsonResponse
from django.db import transaction
from django.views.generic import View
from django.contrib.auth import login

from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from account.models import User
from center.models import Center


class SignupView(View):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        if not email or password:
            result = {'result':'error', 'error': 'No Required Field', 'error_msg': 'Email, Password는 필수입니다.'}
            return JsonResponse(result)
        phone = request.data['phone']
        is_partner = request.data['is_partner']
        is_partner = True if is_partner == 'true' else False
        if is_partner:
            center = request.data['center']
            center = Center.objects.filter(id=center).first()
            if not center:
                result = {'result':'error', 'error': 'No Required Field', 'error_msg': '직원의 경우 센터 코드는 필수입니다.'}
            return JsonResponse(result)
        else:
            center = None
        name = request.data['name']
        nick_name = request.data['nick_name']

        user = User.objects.filter(email=email).first()
        if user:
            result = {'result':'error', 'error': 'User Exist', 'error_msg': '동일한 이메일을 가진 유저가 존재합니다.'}
            return JsonResponse(result)
        sid = transaction.savepoint()
        try:
            with transaction.atomic():
                user = User(
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