import os,sys
sys.path.append('/Users/User/Desktop/은행 고객 이탈/Bank-Churn2/Bank-Churner-Prediction/')
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline, Pipeline
from lightgbm import LGBMClassifier
from imblearn.over_sampling import SMOTE
from sklearn import metrics
from churner.models.user_model import get_user

# 데이터 불러오기
CSV_FILEPATH = os.path.join(os.getcwd(), 'BankChurners.csv')

# 예측모델
def predict_card(username):
    data = pd.read_csv(CSV_FILEPATH)
    columns = ['Attrition_Flag','Contacts_Count_12_mon',  'Total_Relationship_Count', 'Customer_Age', 'Gender', 'Dependent_count', 'Education_Level', 'Income_Category']
    data = data[columns]
    

    # 데이터 전처리
    data = data[data['Income_Category'] != 'Unknown'] 
    data = data[data['Education_Level'] != 'Unknown'] 

    # encoding
    data['Attrition_Flag'] = data['Attrition_Flag'].replace({'Attrited Customer':1, 'Existing Customer':0})
    data['Gender'] = data['Gender'].replace({'F':1, 'M':0})
    

    # Oridinal Encoding

    Income_Category_map = {
        'Less than $40K' : 0,
        '$40K - $60K'    : 1,
        '$60K - $80K'    : 2,
        '$80K - $120K'   : 3,
        '$120K +'        : 4
    }


    Education_Level_map = {
        'Uneducated'    : 0,
        'High School'   : 1,
        'College'       : 2,
        'Graduate'      : 3,
        'Post-Graduate' : 4,
        'Doctorate'     : 5
        }

    data.loc[:, 'Income_Category'] = data['Income_Category'].map(Income_Category_map)
    data.loc[:, 'Education_Level'] = data['Education_Level'].map(Education_Level_map)

    # Customer_Age 70세 이상 데이터 제외(2명)
    data = data[data['Customer_Age'] < 70]

    
    # 타겟 설정 및 데이터 나누기
    target = 'Attrition_Flag'
    features = data.drop(columns= target).columns

    train, test = train_test_split(data, test_size = 0.2, random_state = 2021, stratify = data[target])
    X_train = train[features]
    y_train = train[target]
    X_test = test[features]
    y_test = test[target]

    # SMOTE로 데이터 불균형 해결
    sm = SMOTE(random_state=2021)

    # train데이터를 넣어 복제함
    X_train_over,y_train_over = sm.fit_resample(X_train,y_train)
    

    # Modeling , RandomseachCV 파라미터

    lgbm_pipe = Pipeline([('lgbm',
                 LGBMClassifier(boosting_type='gbdt',
                                class_weight=None,
                                colsample_bytree=0.9596227748175055,
                                importance_type='split',
                                learning_rate=0.0552306312599236, max_depth=7,
                                min_child_samples=20, min_child_weight=0.001,
                                min_split_gain=0.0, n_estimators=470, n_jobs=-1,
                                num_leaves=31, objective='binary',
                                random_state=2021, reg_alpha=0.0,
                                reg_lambda=0.0,
                                scale_pos_weight=0.2638602390113117,
                                silent=True, subsample=1.0,
                                subsample_for_bin=200000, subsample_freq=0))],
                                verbose=False)
            

    lgbm_pipe.fit(X_train_over,y_train_over)
    
    
    user = get_user(username)
    
    ex = {'Customer_Age':user.age, 'Gender':user.gender, 'Dependent_count':user.dependent, 'Education_Level':user.Edu_Level, 'Total_Relationship_Count':user.total_rel ,'Contacts_Count_12_mon':user.contact, 'Income_Category':user.income}
    ex = pd.DataFrame(data[ex], index = [0])
    prediction = lgbm_pipe.predict(ex)[0]
    
    return prediction

def msg_processor(msg_code):
    '''
    msg_processor returns a msg object with 'msg', 'type'
    where 'msg' corresponds to the message user sees
    and 'type' is the color of the alert element

    codes:
        - 0 : Successfully added to database
        - 1 : User does not exist
        - 2 : Successfully deleted user
    '''

    msg_code = int(msg_code)

    msg_list = [
        (
            'Successfully added to database',
            'success'
        ),
        (
            'somthing wrong',
            'warning'
        ),
        (
            'Successfully deleted user',
            'info'
        )
    ]

    return {
        'msg':msg_list[msg_code][0],
        'type':msg_list[msg_code][1]
    }