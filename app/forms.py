from os import listdir
from os.path import isdir, join
from flask_wtf import Form
from wtforms import TextField, PasswordField, SelectField, TextAreaField, SubmitField, BooleanField, validators, ValidationError
from wtforms.validators import Required

#Identify network in inventory directory
inv_dir =  "inventory/"
net_inventory = [f for f in listdir(inv_dir) if isdir(join(inv_dir, f))]

class NewDevice(Form):
    device = TextField("Device Name", [validators.Required()])
    mgmt_ip = TextField("Management IP", [validators.Required()])
    role = TextField("Device Role", [validators.Required()])
    network = SelectField(u'Network', choices=[(f, f) for f in net_inventory])
    username = TextField("Login Username", [validators.Required()])
    password = PasswordField("Login Password", [validators.Required()])
    submit = SubmitField("Submit")


class NewNetwork(Form):
    network = TextField("Network", [validators.Required()])
    roles = TextField("Device Roles", [validators.Required()])
    username = TextField("Login Username", [validators.Required()])
    password = PasswordField("Login Password", [validators.Required()])
    submit = SubmitField("Submit")

