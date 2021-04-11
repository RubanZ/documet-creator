# -*- coding: utf-8 -*- 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

application = Flask(__name__)
application.config.from_object(Config)


database = SQLAlchemy(application)


from app import routes, models




# def uploadBD():
#     f = open("export_user.json", "r", encoding="utf-8")
#     js = json.loads(f.read())
#     for upd in js:

#         user = Users.query.filter_by(email=upd["email"]).first()
        
#         user.createdAt = upd['createdAt']
        
#         database.session.commit()