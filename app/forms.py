from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class SearchForm(Form):
	videoid = StringField('videoid', validators = [DataRequired()])
