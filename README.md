# Bank-Churner-Prediction
> version 1.0 : https://backchurn3.herokuapp.com/

## 고객 이탈 방지를 위한 모델링 및 웹 서비스 구현

## 목차

- [Bank-Churner-Prediction](#bank-churner-prediction)
  - [고객 이탈 방지를 위한 모델링 및 웹 서비스 구현](#고객-이탈-방지를-위한-모델링-및-웹-서비스-구현)
  - [목차](#목차)
    - [프로젝트 선정 이유](#프로젝트-선정-이유)
    - [Dataset](#dataset)
    - [변수 설명](#변수-설명)
    - [Skils](#skils)
    - [모델 검증, 결과](#모델-검증-결과)
    - [시각화](#시각화)
    - [Web application](#web-application)

***

### 프로젝트 선정 이유

- 2019년 말부터 오픈뱅킹 서비스의 시작으로, 현재는 은행, 증권사 뿐만아니라 다양한 핀테크 업체들이 금융 서비스를 제공하고있습니다. 
- 그에 따라 고객의 선택지가 다양해졌고 그에 따라 이탈률이 증가하고 있기 때문에, 고객 이탈 방지 전략에 도움이 될만한 결과를 찾기 위해 해당 프로젝트를 진행했습니다.

***
<br>

### Dataset

- Kaggle(https://www.kaggle.com/sakshigoyal7/credit-card-customers)

***
<br>

### 변수 설명

- CLIENTNUM : 고객 번호. 계정을 보유한 고객의 고유 식별자
- **Attrition_Flag(Target) : 고객 이탈 여부, 1 - Churner/ 0 - non Churner**
- Customer_Age : 고객의 나이
- Gender : 성별, M=Male, F=Female
- Dependent_count : 부양가족수
- Education_Level : 고객의 학력
- Marital_Status : Married, Single, Divorced, Unknown
- Income_Category : 연간 소득 (40K, 40K - 60K, 60K - 80K, 80K-120K, 120K+ )
- Card_Category : 카드 등급 (Blue, Silver, Gold, Platinum)
- Months_on_book : 은행과 거래 기간
- Total_Relationship_Count : 고객이 보유한 총 상품 수
- Months_Inactive_12_mon : 최근 12개월 동안 비활성 개월 수
- Contacts_Count_12_mon : 최근 12개월 동안 연락한 횟수
- Credit_Limit : 신용 한도
- Total_Revolving_Bal : 총 리볼빙(일부결제금액이월약정) 잔액
- Avg_Open_To_Buy : 작년 평균 카드 Open to buy(신용한도-계좌잔액)
- Total_Amt_Chng_Q4_Q1 : 거래 금액의 변화 (1분기 대비 4분기)
- Total_Trans_Amt : 최근 12개월 총 거래 금액
- Total_Trans_Ct : 최근 12개월 총 거래 횟 수
- Total_Ct_Chng_Q4_Q1 : 1분기 대비 4분기 거래번호 변경 수
- Avg_Utilization_Ratio : 평균 카드 사용률
- cb_person_gist_length : 첫 대출 받은 후 지난 기간(연 단위)

***
<br>

### Skils

- EDA & Preprocessing : pandas, numpy, matploylib, plotly, seaborn, profiling
- Modeling : lightgbm, adaboost,random forest, SMOTE, sklearn, CV
- Visualization : PDP, Shap
- Web : Flask, SQLAlchemy, HTML, Migrate, gunicorn, heroku

***
<br>

### 모델 검증, 결과

![image](https://user-images.githubusercontent.com/76996686/133222780-9c0e9be0-967d-49b9-9360-e57a5338655f.png)

<br>

- ROC 곡선 : FPR의 변화에 따른 TPR의 변화를 나타내는 곡선
  - FPR : 실제 값 Negative를 Postive라고 잘못 예측하는 수준
  - TPR : 실제 값 Positive가 정확하게 예측되야 하는 수준

- AUC Score : ROC 곡선 밑의 면적
  - 1에 가까울 수록 좋은 수치
  - 곡선 밑의 면적의 합

***
<br>

### 시각화

![image](https://user-images.githubusercontent.com/76996686/133258625-f3fd50f4-8ffd-42f3-beca-7d80a2f51e0f.png)

- Total_Trans_Amt 특성은 6000달러를 기준으로 총 거래 금액이 기준 금액 이하일 수록 이탈률이 낮고, 기준 금액 이상부터 약 8000달러 까지 이탈률이 증가했다가 점점 떨어진다.

![image](https://user-images.githubusercontent.com/76996686/133258727-2d75dd39-c0ac-41a0-8642-3777e4929c0f.png)

- Total_Trans_Ct 특성은 약 50회 전까지는 이탈률에 큰 영향을 끼치지 않지만 50회 이후 부터 이탈률을 낮추는데 큰 영향을 끼친다.

![image](https://user-images.githubusercontent.com/76996686/133258978-2ae331b4-74b5-47bf-9972-915d21912957.png)

- Dependent_count 특성은 부양 가족이 많을 수록 이탈률이 증가하다 3명이상 부터는 큰 변화가 없다

***
<br>

### Web application

![image](https://user-images.githubusercontent.com/76996686/133262174-e96a8407-aba0-4aa0-b83a-65923d2b4521.png)

![image](https://user-images.githubusercontent.com/76996686/133262363-7cef38c0-f55f-4d2c-b90d-addba7c7a0e8.png)



***
<br>


[위로가기](#목차)
