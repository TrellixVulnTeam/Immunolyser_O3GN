from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, MultipleFileField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from flask_wtf.file import FileField, FileRequired, DataRequired

class InitialiserForm(FlaskForm):
    col_name = StringField("Peptide Column", validators=[DataRequired(),Length(min=2,max=55)])
    file_input = MultipleFileField("Peptide File", validators=[DataRequired()])
    submit = SubmitField("Register Now")