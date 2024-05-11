# models/ssh_connection.py

import paramiko

class SSHConnection:
    @staticmethod
    def execute_ssh_command(host, port, username, password, command):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            client.connect(host, port=port, username=username, password=password)
            stdin, stdout, stderr = client.exec_command(command)
            output = stdout.read().decode('utf-8')
            error = stderr.read().decode('utf-8')
            client.close()
            return output, error
        except Exception as e:
            return None, str(e)
