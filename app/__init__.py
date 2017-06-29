import os
import sys

sys.path.insert(0, '/srv/netmgmt/library')
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from forms import NewDevice, NewNetwork
from device_group_mgmt import device_add, network_add

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
    # Form Data from forms
    device_form = NewDevice()
    device_name = device_form.device.data
    mgmt_ip = device_form.mgmt_ip.data
    role = device_form.role.data
    network = device_form.network.data
    username = device_form.username.data
    password = device_form.password.data
    message = None

    if request.method == 'POST':
        if device_form.validate() == False:
            flash('All fields are required.', 'error')
            return render_template('newdevice.html', form=device_form)
        else:
            try:
                output = device_add(device_name, mgmt_ip, role, network, username, password)
                flash('Sucess! ' + output, 'success')
            except :
                flash('Failed: Unable to add device', 'error')
        return render_template('newdevice.html', form=device_form, error=message)

    elif request.method == 'GET':
        return render_template('newdevice.html', form=device_form)


@app.route('/newnetwork', methods=['GET', 'POST'])
def newnetwork():
    # Form Data from forms
    network_form = NewNetwork()
    roles = network_form.roles.data
    network = network_form.network.data
    username = network_form.username.data
    password = network_form.password.data
    message = None

    if request.method == 'POST':
        if network_form.validate() == False:
            flash('All fields are required.', 'error')
            return render_template('newnetwork.html', form=network_form)
        else:
            try:
                output = network_add(network, roles, username, password)
                flash('Sucess! ' + output, 'success')
            except:
                flash('Failed: Unable to add network', 'error')
        return render_template('newnetwork.html', form=network_form, error=message)

    elif request.method == 'GET':
        return render_template('newnetwork.html', form=network_form)

if __name__ == '__main__':
    app.run(debug=True)
