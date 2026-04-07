from flask_wtf import FlaskForm
import wtforms


class SignUp(FlaskForm):
    username = wtforms.StringField(
        label="Введіть Ваш логін",
        validators=[wtforms.validators.DataRequired(), wtforms.validators.length(min=3, max=1000)]
    )
    first_name = wtforms.StringField(label="Ім'я (не обов'язково)")
    last_name = wtforms.StringField(label="Прізвище (не обовязково)")
    password = wtforms.PasswordField(
        label="Пароль",
        validators=[wtforms.validators.DataRequired(), wtforms.validators.length(min=6)]
    )
    submit = wtforms.SubmitField(label="Зареєструватись")


class SignIn(FlaskForm):
    username = wtforms.StringField(label="Логін", validators=[wtforms.validators.DataRequired()])
    password = wtforms.PasswordField(label="Пароль", validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField(label="Вхід")


class PostForm(FlaskForm):
    title = wtforms.StringField(
        label="Назва статті",
        validators=[wtforms.validators.DataRequired(), wtforms.validators.length(min=1, max=1000)]
    )
    text = wtforms.TextAreaField(
        label="Стаття",
        validators=[wtforms.validators.DataRequired(), wtforms.validators.length(min=10)]
    )
    image = wtforms.FileField(label="Картинка")
    submit = wtforms.SubmitField(label="Додати статтю")