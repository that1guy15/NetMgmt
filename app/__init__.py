import os
import sys
sys.path.insert(0,'/srv/netmgmt/library')
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from forms import NewDevice
from device_group_mgmt import device_add


app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'password'
playbook_path = 'playbooks/'
newdevice_playbook = 'add-network-inventory.yml'

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/inventory')
def inventory():
  return render_template('home.html')

@app.route('/newdevice', methods=['GET', 'POST'])
def newdevice():
    device_form = NewDevice()
    error = None

    if request.method == 'POST':
        if device_form.validate() == False:
            flash('All fields are required.', 'error')
            return render_template('newdevice.html', form=device_form)
        else:
            device_name = device_form.device.data
            mgmt_ip = device_form.mgmt_ip.data
            role = device_form.role.data
            network = device_form.network.data
            username = device_form.username.data
            password = device_form.password.data
            output = device_add(device_name, mgmt_ip, role, network, username, password)
            flash('Sucess! ' + output, 'success')
        return render_template('newdevice.html', form=device_form, output=output, error=error)

    elif request.method == 'GET':
        return render_template('newdevice.html', form=device_form)

if __name__ == '__main__':
  app.run(debug=True)
