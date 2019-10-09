import paramiko
from sys import argv

import paramiko
import sys

nbytes = 4096
port = 22
username = 'pi' 
password = 'raspberry'
command = 'python3 /home/pi/Desktop/4OI6/state_machine.py'

def line_buffered(f):
    line_buf = ""
    while not f.channel.exit_status_ready():
        line_buf += f.read(1)
        if line_buf.endswith('\n'):
            yield line_buf
            line_buf = ''

def SSH_session(SSH_adr):
    ssh_session = paramiko.SSHClient()
    ssh_session.load_system_host_keys()
    ssh_session.connect(SSH_adr, username=username, password=password, timeout = 10)

    stdin, stdout, stderr = ssh_session.exec_command(command)
    
    for l in line_buffered(stdout):      
        print(l)

    ssh_session.close()

def argument_handler():
    if len(argv) != 2:
        print("Missing input argument ...\n")

    SSH_adr = argv[1]
    SSH_session(SSH_adr)

if __name__ == "__main__":
    argument_handler()
