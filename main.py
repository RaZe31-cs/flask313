from flask import Flask, render_template, url_for, redirect
from data import db_session
from data.jobs import Jobs
from data.users import User
from reg_form import Reg_form


app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/', methods=['GET', 'POST'])
def index():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    form = Reg_form()
    if form.validate_on_submit():
        print('Пуск')
        user = User()
        user.surname = form.surname.data
        user.name = form.name.data
        user.age = form.age.data
        user.position = form.position.data
        user.speciality = form.speciality.data
        user.address = form.address.data
        user.email = form.login_or_email.data
        user.hashed_password = form.password.data
        db_sess.add(user)
        db_sess.commit()
        return redirect('/success')
    return render_template('index.html', form=form)


@app.route('/success')
def success():
    return 'Вы успешно зарегистрированы'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
