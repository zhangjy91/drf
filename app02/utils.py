
def my_jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token':token,
        'msg':'登录成功',
        'status':100,
        'username':user.username,

    }


from rest_framework.authentication import BaseAuthentication
from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_jwt.authentication import jwt_decode_handler
import jwt

from drf_day12.models import User


class MyJwtAuthentication(BaseAuthentication):
    def authenticate(self, request):
        jwt_value = request.META.get('HTTP_AUTHORIZATION')
        if jwt_value:
            try:
                payload = jwt_decode_handler(jwt_value)
            except jwt.ExpiredSignature:
                raise AuthenticationFailed('签名过期')
            except jwt.InvalidTokenError:
                raise AuthenticationFailed('用户非法')
            except Exception as e:
                raise AuthenticationFailed(str(e))
            print(payload)

            # user = User.objects.get(pk=payload.get('user_id'))

            user = User(id=payload.get('user_id'), username=payload.get('username'))

            return user, jwt_value
        
        raise AuthenticationFailed('你没有携带认证信息')