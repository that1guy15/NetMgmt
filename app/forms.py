from os import listdir
from os.path import isfile, join
from flask_wtf import Form
from wtforms import TextField, SelectField, TextAreaField, SubmitField, BooleanField, validators, ValidationError
from wtforms.validators import Required

 
class NewDevice(Form):
  device = TextField("Device", [validators.Required()])
  mgmt_ip = TextField("Management IP", [validators.Required()])
  role = TextField("Device Role", [validators.Required()])
  network = TextField("Network", [validators.Required()])
  username = TextField("Login Username", [validators.Required()])
  password = TextField("Login Password", [validators.Required()])
  submit = SubmitField("Submit")

