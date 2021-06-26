from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_required, login_user
from werkzeug.urls import url_parse
from flask import url_for, request
import forms
import User

app = Flask(__name__)
app.secret_key = 's3cr3t'
bootstrap = Bootstrap()
bootstrap.init_app(app)
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    user = User.User()
    return user

@app.route('/home')
def home():
    return "hello"


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm()
        print(form.submit.data)
        print (form.validate_on_submit())
        if form.validate_on_submit():
            # user = User.User()
            # login_user(user)
            if form.submit.data == True:
                return redirect('http://www.baidu.com')

    return render_template('index.html',form=form)

@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run()
