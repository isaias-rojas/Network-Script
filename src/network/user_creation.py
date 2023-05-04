
class UserManager:
    def __init__(self, remote_command_executor):
        self.remote_command_executor = remote_command_executor

    def create_user(self, username, password):
        command = f"useradd {username} -p {password}"
        return self.remote_command_executor.execute_sudo_command(command)

    def add_user_to_sudo(self, username):
        sudo_command = f"usermod -aG sudo {username}"
        return self.remote_command_executor.execute_sudo_command(sudo_command)
