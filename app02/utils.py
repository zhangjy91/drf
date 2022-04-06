
def my_jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token':token,
        'msg':'登录成功',
        'status':100,
        'username':user.username,

    }