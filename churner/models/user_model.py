import os,sys
sys.path.append('/Users/User/Desktop/은행 고객 이탈/Bank-Churn2/Bank-Churner-Prediction/')
from churner import db

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(64), nullable = False)
    age = db.Column(db.Integer(), nullable = False)
    gender = db.Column(db.Integer(), nullable = False)
    dependent = db.Column(db.Integer(), nullable = False)
    Edu_Level = db.Column(db.Integer(), nullable = False)
    contact = db.Column(db.Integer(), nullable = False, default="0")
    total_rel = db.Column(db.Integer(), nullable = False, default="0")
    income = db.Column(db.Integer(), nullable = False)
    
    def __repr__(self):
        return f"User {self.user_id}, {self.username}, {self.age}, {self.gender}, {self.total_rel}, {self.dependent}, {self.Edu_Level}, {self.contact}, {self.income}"


def add_user(raw_user) :
    
    new_user = User(
        username = raw_user['username'],
        age = raw_user['age'],
        gender = raw_user['gender'],
        dependent = raw_user['dependent'],
        Edu_Level = raw_user['Edu_Level'],
        contact = raw_user['contact'],
        total_rel = raw_user['total_rel'],
        income = raw_user['income']
        )
    
    if User.query.filter(User.username == new_user.username).first() == None :
        db.session.add(new_user)
        db.session.commit()
    return User.query.filter(
            (User.username == new_user.username) 
            and (User.age == new_user.age) 
            and (User.Edu_Level == new_user.Edu_Level)
            and (User.contact == new_user.contact)
            ).first()

def get_users() :
    return User.query.all()

def get_user(username):
    return User.query.filter(User.username == username).first()

def get_user_id(user_id):
    return User.query.filter(User.user_id == user_id).first()

def delete_user(user_id) :
    user = User.query.filter(User.user_id == user_id).first()
    db.session.delete(user)
    db.session.commit()

