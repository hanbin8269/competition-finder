import json
import bcrypt
import jwt
from django.views import View
from django.http import JsonResponse , HttpResponse
from .models import User
from competition_finder.settings import SECRET_KEY

class JoinView(View):
    def post(self, request):
        data = json.loads(request.body)

        # ==== 비밀번호 암호화 ====
        password = data['password'].encode('utf-8')                 # 입력된 패스워드를 바이트 형태로 인코딩
        password_crypt = bcrypt.hashpw(password, bcrypt.gensalt())  # 암호화된 비밀번호 생성
        password_crypt = password_crypt.decode('utf-8') 
        # =========================
        
        # =======저장=======
        User(
            email = data['email'],
            nickname = data['nickname'],
            password = password_crypt 
        ).save()
        #===================

        return JsonResponse({'message' : '회원가입 완료'},status = 200)

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(email = data['email']).exists():
                user = User.objects.get(email = data['email'])

                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                    #----------토큰 발행--------
                    token = jwt.encode({'email' : data['email']},SECRET_KEY, algorithm="HS256")
                    token = token.decode('utf-8')
                    #--------------------------
                    return JsonResponse({'token':token},status = 200)
            return JsonResponse({'message' : '등록되지 않은 이메일 입니다.'},status = 200)
        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEYS'}, status = 400)

# 유저들 목록 조회하는 뷰 ( 배포 시 삭제 )
class UserLookupView(View):
    def get(self,request):
        users = User.objects.all().values()
        print(users)
        return JsonResponse({'users' : str(users)}, status = 200)

class TokenCheckView(View):
    def post(self, request):
        data = json.loads(request.body)

        decoded_token = jwt.decode(data['token'], SECRET_KEY, algorithm = 'HS256')

        if User.objects.filter(email = decoded_token['email']).exists():
            return HttpResponse(status = 200)
        return HttpResponse(status = 403)
        