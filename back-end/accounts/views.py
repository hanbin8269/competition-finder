import json
from django.views import View
from django.http import JsonResponse
from .models import User

class JoinView(View):
    def post(self, request):
        data = json.loads(request.body)
        User(
            email = data['email'],
            nickname = data['nickname'],
            password = data['password']
        ).save()

        return JsonResponse({'message' : '회원가입 완료'},status = 200)

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        if User.objects.filter(email = data['email']).exists():
            user = User.objects.get(email = data['email'])
            if user.password == data['password']:
                return JsonResponse({'message' : f'{user.email}님 로그인 성공!'},status = 200)
            else :
                return JsonResponse({'message' : '비밀번호가 틀렸어요'},status = 200)
        return JsonResponse({'message' : '등록되지 않은 이메일 입니다.'},status = 200)
            
        