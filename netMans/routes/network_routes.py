from flask import Blueprint, render_template, request, send_from_directory,redirect, url_for,jsonify
from models.network_scanner import get_local_ip_range, scan_network
from models.packet_sniffer import sniff_packets
from models.network_bandwidth import get_network_bandwidth
from models.ssh_connection import SSHConnection

import os

network_blueprint = Blueprint('network', __name__)

@network_blueprint.route('/')
def home():
    return render_template('home.html')

@network_blueprint.route('/start_scan', methods=['GET', 'POST'])
def start_scan():
    if request.method == 'POST':
        target_ip_range = get_local_ip_range()
        devices = scan_network(target_ip_range)
        return render_template('scan_network.html', devices=devices)
    return render_template('start_scan.html')

@network_blueprint.route('/start_sniffing', methods=['GET', 'POST'])
def start_sniffing():
    if request.method == 'POST':
        packets, filename = sniff_packets()
        return render_template('sniff_results.html', packets=packets, filename=filename)
    return render_template('start_sniffing.html')

@network_blueprint.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(os.path.abspath("."), filename, as_attachment=True)

@network_blueprint.route('/network_bandwidth')
def monitor_network_bandwidth():
    network_stats = get_network_bandwidth()
    return render_template('network_bandwidth.html', network_stats=network_stats)

@network_blueprint.route('/execute_ssh_command', methods=['GET', 'POST'])
def execute_ssh_command():
    if request.method == 'POST':
        host = request.form['host']
        port = int(request.form['port'])
        username = request.form['username']
        password = request.form['password']
        command = request.form['command']

        output, error = SSHConnection.execute_ssh_command(host, port, username, password, command)
        
        if error:
            return jsonify({'error': error}), 500
        else:
            return jsonify({'output': output}), 200
    elif request.method == 'GET':
        return render_template('execute_ssh_command.html')





