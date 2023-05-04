from network.ssh_connection import SSHConnection
from network.command_executor import RemoteCommandExecutor
from network.user_creation import UserManager

host = input("Enter the remote machine IP: ")
username = input("Enter your username: ")
password = input("Enter your password: ")
port = input("Enter the SSH port number (default is 22): ")

if port:
    port = int(port)
else:
    port = 22

ssh_connection = SSHConnection(host, username, password, port)
ssh_connection.connect()
remote_command_executor = RemoteCommandExecutor(ssh_connection)

while True:
    choice = input("Enter 1 to execute a command, 2 to create a new user, or 3 to exit: ")
    if choice == "1":
        option = input("Enter 1 to execute netstat, 2 to execute nslookup,  3 to enter a custom command or 4 to execute a sudo command: ")
        if option == "1":
            output = remote_command_executor.execute_netstat()
            print(output)
        elif option == "2":
            hostname = input("Enter the hostname to lookup: ")
            output = remote_command_executor.execute_nslookup(hostname)
            print(output)
        elif option == "3":
            command = input("Enter the command to execute: ")
            output = remote_command_executor.execute_command(command)
            print(output)
        elif option == "4":
            command = input("Enter the sudo command to execute. Please take into consideration that for sudo commands you dont need to put sudo, just the command: ")
            output = remote_command_executor.execute_sudo_command(command)
            print(output)
        else:
            print("Invalid option.")

    elif choice == "2":
        username = input("Enter the username of the new user: ")
        password = input("Enter the password for the new user: ")
        user_manager = UserManager(remote_command_executor)
        output = user_manager.create_user(username, password)
        option = input("Enter 1 to add the user to the sudo group, or 2 to skip: ")
        if option == "1":
            output = user_manager.add_user_to_sudo(username)
            print(output)
        elif option == "2":
            pass
        else:
            print("Invalid option.")
        # Print the output of the command
        print(output)

    elif choice == "3":
        ssh_connection.close_connection()
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")