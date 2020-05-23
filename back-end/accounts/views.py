import json
from django.views import View
from django.http import JsonResponse
from .models import User

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        User(
            email = data['email'],
            nickname = data['nickname'],
            password = data['password']
        ).save()

        return JsonResponse({'message' : '회원가입 완료'},status = 200)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)
        