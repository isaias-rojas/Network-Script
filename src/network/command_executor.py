class RemoteCommandExecutor:
    def __init__(self, ssh_connection):
        self.ssh_connection = ssh_connection
        self.password = ssh_connection.password

    def execute_command(self, command):
        return self.ssh_connection.execute_command(command)

    def execute_sudo_command(self, command):
        command = f"sudo -S {command}"
        command_with_password = f"echo '{self.password}' | {command}"
        print(command_with_password)
        return self.execute_command(command_with_password)

    def execute_netstat(self):
        command = "netstat"
        return self.execute_command(command)

    def execute_nslookup(self, domain):
        command = f"nslookup {domain}"
        return self.execute_command(command)

