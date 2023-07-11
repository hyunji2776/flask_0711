from flask import Blueprint

hyunji = Blueprint('myname',__name__, url_prefix='/hyunji')
#basic : 우리가 부르는 별명
#__name__ : flask 프레임워크가 찾을 이름
#prefix : 라우팅 주소

@hyunji.route('/about_me')
def about_me():
    return f'저는 {__name__} 입니다'

@hyunji.route('/hello')
def hello():
    return f'안녕하세요'

@hyunji.route('/bye')
def bye():
    return f'잘 가세요'