import os
import requests
import paramiko
import socket
import time

host = socket.gethostbyname("fpp.local")
port = 22
cwd = os.getcwd()
transport = paramiko.Transport((host, port))


password  = "falcon"
username = "fpp"
transport.connect(username=username, password=password)

sftp = paramiko.SFTPClient.from_transport(transport)

def printTotals(transferred, toBeTransferred):
    speed = 0
    KB_transferred = transferred * 0.001
    KB_to_be_transferred = toBeTransferred * 0.001
    print (f"Transferred: {KB_transferred:.2f}\tOut of: {KB_to_be_transferred:.2f} \t{speed}", end="\r")
    time.sleep(1)

# for file in os.listdir():
#     if file.endswith(".fseq"):
#         path = os.path.join("/home/fpp/media/sequences", file)
#         local = os.path.join(cwd, file)
#         sftp.put(localpath=local, remotepath=path, callback=printTotals)
#         print(path)

sftp.close()

session = transport.open_channel(kind="session")
session.exec_command('touch hello_world')

transport.close()
