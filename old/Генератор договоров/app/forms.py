from flask_wtf import FlaskForm
from wtforms import StringField, FieldList, PasswordField, BooleanField, SubmitField, BooleanField, IntegerField, SelectField, DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Optional


class LoginForm(FlaskForm):
    email = StringField('Электронная почта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')