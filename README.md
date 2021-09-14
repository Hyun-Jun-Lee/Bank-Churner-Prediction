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

> 프로젝트 시작 계기

- 2019년 말부터 오픈뱅킹 서비스의 시작으로, 현재는 은행, 증권사 뿐만아니라 다양한 핀테크 업체들이 금융 서비스를 제공하고있습니다. 
- 그에 따라 고객의 선택지가 다양해졌고 그에 따라 이탈률이 증가하고 있기 때문에, 고객 이탈 방지 전략에 도움이 될만한 결과를 찾기 위해 해당 프로젝트를 진행했습니다.


> 모델링 성능

![image](https://user-images.githubusercontent.com/76996686/133222780-9c0e9be0-967d-49b9-9360-e57a5338655f.png)


