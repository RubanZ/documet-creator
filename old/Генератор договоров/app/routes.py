from flask import render_template, flash, redirect, send_file
from flask_login import LoginManager, current_user, login_user, logout_user, login_required


from docx import Document
from io import StringIO


from app import application
from app import database
from app.models import Users

from app.forms import LoginForm

login = LoginManager(application)
login.login_view = 'login'


@application.route("/")
@login_required
def index():
    return render_template("list.html", title = 'Привет')


@application.route("/d")
@login_required
def generate():
    document = Document()
    document.add_heading("Sample Press Release", 0)
    f = StringIO()
    document.save(f)
    length = f.tell()
    f.seek(0)
    return send_file(f, as_attachment=True, attachment_filename='report.doc')

@login.user_loader
def load_user(id):
    return Users.query.get(int(id))


@application.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        # if user.password_hash is None:
        #     return redirect('/forgot/' + user.email)
            
        # if user is None or not user.check_password(form.password.data):
        #     flash('Неверный email или пароль')
        #     return redirect('/login')
        login_user(user, remember=form.remember_me.data)
        return redirect('/')
    return render_template("login.html", form=form)

@application.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')


@application.route('/ru')
def ru():
    user = Users(username = 'RubanZ', email='ruban_1998@hotmail.com', password_hash = '')
    user.set_password('!Programmist2')
    database.session.add(user)
    database.session.commit()
    return redirect('/login')


# from docxtpl import DocxTemplate

# doc = DocxTemplate("Templates/Акт.docx")
# context = { 'Номер_договора' : "1" }
# doc.render(context)
# doc.save("Result/result.docx")