from ftplib import FTP
from sys import argv
import os.path

def start_FTP_link(FTP_file, pi_FTP_addr, pi_FTP_port):
    try:
        ftp = FTP()
        ftp.connect(pi_FTP_addr, pi_FTP_port, 10)
        ftp.login(user='pi', passwd='raspberry')
        ftp.cwd('/home/pi/Desktop/4OI6/')
        
        filePath, fileName = os.path.split(FTP_file)

        file = open(FTP_file, 'rb')
        ftp.storbinary('STOR ' + fileName, file)
        file.close()

        ftp.quit()
        print("Finished FTP session ...")
    except:
        print("FTP error ...")
        file.close()
        ftp.quit()
        exit()

	
def argument_handler():
    if len(argv) != 4:
        print("Missing input argument ...\n")
        exit()
    
    FTP_file = argv[1]    
    if not os.path.isfile(FTP_file):
        print("Cannot find file: ", FTP_file)
        exit()

    pi_FTP_addr = argv[2]
    pi_FTP_port = int(argv[3])
    start_FTP_link(FTP_file, pi_FTP_addr, pi_FTP_port)
	
	
if __name__ == "__main__":
    argument_handler()
