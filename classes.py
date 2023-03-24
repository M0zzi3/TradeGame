from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField
class RoomCodeForm(Form):

    roomCode_value = StringField('roomCode', [validators.Length(min=4, max=4)])

    submit = SubmitField('Check')
