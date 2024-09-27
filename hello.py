from datetime import datetime, timezone

from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import EmailField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a random and very long string that is long and long and long and repetitive'

bootstrap = Bootstrap(app)
moment = Moment(app)


class UserInfoForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = EmailField('Enter your email address:', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    user_info_form = UserInfoForm()
    if user_info_form.validate_on_submit():
        old_name = session.get('name')
        new_name = user_info_form.name.data
        if old_name is not None and old_name != new_name:
            flash("Looks like you have changed your name!")
        session['name'] = new_name

        old_email = session.get('email')
        new_email = user_info_form.email.data
        if "utoronto" in new_email.lower():
            if old_email is not None and old_email != new_email:
                flash("Looks like you have changed your email!")
        else:
            new_email = None
        session['email'] = new_email

        return redirect(url_for('index'))

    return render_template('index.html', current_time=datetime.now(timezone.utc), username_form=user_info_form, name=session.get('name'), email=session.get('email'))


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
