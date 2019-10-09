import paramiko
from sys import argv
from time import sleep

def SSH_session(SSH_addr):
    ### establish ssh connection
    try:
        ssh_session = paramiko.SSHClient()
        ssh_session.load_system_host_keys()
        ssh_session.connect(SSH_addr, username='pi', password='raspberry', timeout = 10)

        stdin, stdout, stderr = ssh_session.exec_command('python3 /home/pi/Desktop/4OI6/state_machine.py')
        ssh_session.close()

        print("Finished SSH session ...")
    except SSHException:
        print("SSH error...")
        ssh_session.close()
        exit()

def argument_handler():
    if len(argv) != 2:
        print("Missing input argument ...\n")
        exit()

    SSH_adr = argv[1]
    SSH_session(SSH_adr)

if __name__ == "__main__":
    argument_handler()