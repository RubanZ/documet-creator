from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


from app import database



class Users(UserMixin, database.Model):
    __tablename__ = 'Users'
    id = database.Column(database.Integer, primary_key = True, nullable=True)
    username = database.Column(database.String(120))
    email = database.Column(database.String(120))
    password_hash = database.Column(database.String(128), nullable=False)
    



    def __repr__(self):
        return self.username

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)