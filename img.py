import paramiko

# Server details
hostname = 'example.com'
port = 22
username = 'your_username'
password = 'your_password'

try:
    # Create SSH client
    client = paramiko.SSHClient()

    # Automatically add the server's host key (not recommended for production)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the server
    client.connect(hostname, port, username, password)

    # Perform operations on the server
    # For example, you can execute commands using client.exec_command('command')

    print("Connected successfully!")
except paramiko.AuthenticationException:
    print("Authentication failed. Please check your credentials.")
except paramiko.SSHException as e:
    print("SSH connection failed:", str(e))
