import paramiko

host = '192.168.0.30'
user = 'chris'
pwd = 'amiga'

ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host,username=user,password=pwd)
stdin,stdout,stderr=ssh_client.exec_command('hostname; ls -l')
stdout.channel.recv_exit_status()
lines = stdout.readlines()
for line in lines:
    print(line)

ssh_client.close()
