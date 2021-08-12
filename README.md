# Bank-Churner-Prediction

## 고객 이탈 방지를 위한 모델링 및 웹 서비스 구현

> Datast

- Kaggle(https://www.kaggle.com/sakshigoyal7/credit-card-customers)

> **변수 설명**

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

> Skils

- EDA & Preprocessing : pandas, numpy, matploylib, plotly, seaborn, profiling
- Modeling : lightgbm, adaboost,random forest, SMOTE, sklearn, CV
- Visualization : PDP, Shap
- Web : Flask, SQLAlchemy, HTML, Migrate, gunicorn, heroku

> Presentation

- 
