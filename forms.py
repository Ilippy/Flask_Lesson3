from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, DateField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo


# Имя пользователя (обязательное поле)
# Электронная почта (обязательное поле, с валидацией на корректность ввода email)
# Пароль (обязательное поле, с валидацией на минимальную длину пароля)
# Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
class RegFormT4(FlaskForm):
    name = StringField('Имя пользователя', validators=[DataRequired()])
    email = EmailField('Электронная почта', validators=[Email()])
    password = PasswordField('Пароль', validators=[Length(min=6, max=20)])
    repeat_password = PasswordField('Подтверждение пароля', validators=[EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')


# имя, электронная почта,пароль (с подтверждением), дата рождения, согласие на обработку персональных данных.
class RegFormT5(FlaskForm):
    name = StringField('Имя пользователя', validators=[DataRequired()])
    email = EmailField('Электронная почта', validators=[Email()])
    password = PasswordField('Пароль', validators=[Length(min=6, max=20)])
    repeat_password = PasswordField('Подтверждение пароля', validators=[EqualTo('password')])
    birth_date = DateField('Дата рождения', format='%Y-%m-%d')
    consent = BooleanField('Согласие на обработку персональных данных', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')

