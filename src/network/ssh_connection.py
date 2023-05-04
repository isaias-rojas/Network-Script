import paramiko

class SSHConnection:
    def __init__(self, host, username, password, port=3022):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        self.ssh_client.connect(hostname=self.host, username=self.username, password=self.password, port=self.port)

    def execute_command(self, command):
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        return stdout.read().decode()

    def close_connection(self):
        self.ssh_client.close()