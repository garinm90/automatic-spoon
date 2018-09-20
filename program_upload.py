import os
import requests
import paramiko
import socket
import time

host = socket.gethostbyname("fpp-2.local")
port = 22
cwd = os.getcwd()
transport = paramiko.Transport((host, port))
play = os.path.join(cwd, 'play')
password  = "falcon"
username = "fpp"
schedule = "1,play,7,00,00,00,24,00,00,1,2014-01-01,2099-12-31,"
playlist_name = "play"



transport.connect(username=username, password=password)
session = transport.open_channel(kind="session")
session.exec_command('rm -r /home/fpp/media/sequences/*\n\
                    rm -r /home/fpp/media/playlists/*\n\
                    rm -f /home/fpp/media/schedule')


sftp = paramiko.SFTPClient.from_transport(transport)

def generate_playlist():
    f = open(playlist_name, "w+")
    f.write("0,0,\n")
    for sequence in os.listdir():
        if sequence.endswith(".fseq"):
            f.write(f's,{sequence},\n')
    f.close()

def generate_schedule():
    f = open("schedule", "w+")
    f.write(schedule)
    f.close

def upload_files():
    for file in os.listdir():
        if file.endswith(".fseq"):
            path = os.path.join("/home/fpp/media/sequences", file)
            local = os.path.join(cwd, file)
            sftp.put(localpath=local, remotepath=path, callback=printTotals)
        elif file == playlist_name:
            path = os.path.join("/home/fpp/media/playlists", file)
            local = os.path.join(cwd, file)
            sftp.put(localpath=local, remotepath=path, callback=printTotals)
        elif file == "schedule":
            path = os.path.join("/home/fpp/media/", file)
            local = os.path.join(cwd, file)
            sftp.put(localpath=local, remotepath=path, callback=printTotals)
        # else:
        #     return "Completed"


def printTotals(transferred, toBeTransferred):
    KB_transferred = transferred * 0.001
    KB_to_be_transferred = toBeTransferred * 0.001
    percentage = transferred / toBeTransferred * 100
    print(f"Transferred: {KB_transferred:.2f}\tOut of: {KB_to_be_transferred:.2f}\t {percentage:.0f}%", end="\r")
    time.sleep(.1)
    
    
generate_playlist()
generate_schedule()
upload_files()
sftp.close()
session = transport.open_channel(kind="session")
session.exec_command(f'/opt/fpp/bin.pi/fpp -p {playlist_name}')
transport.close()
