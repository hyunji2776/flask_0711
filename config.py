import os

#db를 저장할 폴더/파일이름



#현재의 경로를 상위 경로로 사용할 것이다
BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'test.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False