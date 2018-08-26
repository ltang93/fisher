from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    # 参数位数验证、设置默认值
    q = StringField(validators=[DataRequired(),Length(min=1,max=30)])
    page = IntegerField(validators=[NumberRange(min=1,max=99)],default=1)