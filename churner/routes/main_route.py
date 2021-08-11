import os,sys
sys.path.append('/Users/User/Desktop/은행 고객 이탈/Bank-Churn2/Bank-Churner-Prediction/')
from flask import Blueprint, render_template, request, redirect, url_for
from churner.models.user_model import get_users, get_user, User
from churner.utils import main_funcs

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/user')
def user_index():
    """
    사용자의 정보를 받아주세요
    """
    msg_code = request.args.get('msg_code', None)
    alert_msg = main_funcs.msg_processor(msg_code) if msg_code is not None else None

    user_list = get_users()
    
    return render_template('user.html', alert_msg=alert_msg, user_list=user_list)


@bp.route('/predict', methods=['GET','POST'])
def compare_index():
    """
    users 에 유저들을 담아 넘겨주세요. 각 유저 항목은 다음과 같은 딕셔너리
    형태로 넘겨주셔야 합니다.
     -  {
            "id" : "유저의 아이디 값이 담긴 숫자",
            "username" : "유저의 유저이름 (username) 이 담긴 문자열"
        }

    prediction 은 다음과 같은 딕셔너리 형태로 넘겨주셔야 합니다:
     -   {
             "result" : "예측 결과를 담은 문자열입니다",
             "compare_text" : "사용자가 넘겨준 비교 문장을 담은 문자열입니다"
         }
    """
    prediction = {}
    username = request.form.get('username', None)

    if request.method == "POST":
        
        user_info = get_user(username)
        try:
            user = username
            result = main_funcs.predict_card(username)
            prediction = {'result':result, "user": user}
        except:
            return redirect(url_for('main.user_index', msg_code=3), code=400)
    return render_template('predict.html', prediction=prediction), 200
