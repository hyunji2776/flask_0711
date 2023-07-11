from flask import Blueprint, render_template
from app.models import Question
from app.models import Answer

fisa = Blueprint('basic',__name__, url_prefix='/fisa')
#basic : 우리가 부르는 별명
#__name__ : flask 프레임워크가 찾을 이름
#prefix : 라우팅 주소

@fisa.route('/about_me')
def about_me():
    return f'저는 {__name__} 입니다'

@fisa.route('/hello')
def hello():
    return f'안녕하세요'

@fisa.route('/bye')
def bye():
    return f'잘 가세요'

@fisa.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get(question_id)
    return render_template('question/question_detail.html', question=question)

@fisa.route('/post')
def post_list():
     question_list = Question.query.all()
     return render_template('question/question_list.html', question_list=question_list)

