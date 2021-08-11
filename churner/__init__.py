import os,sys
sys.path.append('/Users/User/Desktop/은행 고객 이탈/Bank-Churn2/Bank-Churner-Prediction/')
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///prod_db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    '''
    if app.config["ENV"] == 'production':
        app.config.from_object('config.ProductionConfig')
    else:
        app.config.from_object('config.DevelopmentConfig')

    if config is not None:
        app.config.update(config)
    '''

    db.init_app(app)
    migrate.init_app(app, db)

    from churner.routes import (main_route, user_route)
    app.register_blueprint(main_route.bp)
    app.register_blueprint(user_route.bp)

    return app



if __name__ == "__main__":
    app = create_app()
    
    app.run(debug=True)
