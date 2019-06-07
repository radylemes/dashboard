import paramiko

key = paramiko.RSAKey.from_private_key_file('./daniel.pem')

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(hostname='18.218.220.164', username='ubuntu', pkey=key)


commands = [

    'sudo apt-get update -y',
    'sudo apt-get install -y python3-pip',

    'git clone https://github.com/radylemes/dashboard',
    'pip3 install -r dashboard/requirements.txt',
    'python3 dashboard/app.py',

]

for command in commands:
    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read().decode(), stderr.read().decode())