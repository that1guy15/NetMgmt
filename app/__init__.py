import os
from os.path import isfile, join
import sys
import subprocess
import threading
from datetime import datetime
from flask import Flask, render_template
from flask import Flask, render_template, request, flash, jsonify
from forms import NewDevice
from netmiko import ConnectHandler
import ansible.playbook
from ansible import utils


app = Flask(__name__)
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

    if request.method == 'POST':
        if device_form.validate() == False:
            flash('All fields are required.')
            return render_template('newdevice.html', form=device_form)
        else:
            device = device_form.device.data
            mgmt_ip = device_form.mgmt_ip.data
            role = device_form.role.data
            network = device_form.network.data
            username = device_form.username.data
            password = device_form.password.data
            extra_vars = '--extra-vars "device_name=' + device + ' mgmt_ip=' + mgmt_ip + ' role=' + role + ' network=' + network + ' username=' + username + ' password=' + password + '"'
            output = subprocess.check_output(pwd)
        return render_template('results.html', output=output)

    elif request.method == 'GET':
        return render_template('newdevice.html', form=device_form)

if __name__ == '__main__':
  app.run(debug=True)
