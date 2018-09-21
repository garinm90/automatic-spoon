import os
import requests
import paramiko
import socket
import time
import pathlib

password  = "falcon"
username = "fpp"
port = 22

try:
    host = socket.gethostbyname("fpp.local")
except:
    print("Cannot find  controller! Are you connected to the network?")
    time.sleep(10)
    exit()

transport = paramiko.Transport((host, port))
try:
    transport.connect(username=username, password=password)
except:
    print("Connection failed!")
sftp = paramiko.SFTPClient.from_transport(transport)
cwd = os.getcwd()
play = os.path.join(cwd, 'play')
schedule = "1,play,7,00,00,00,24,00,00,1,2014-01-01,2099-12-31,"
playlist_name = "play"
        
    
def delete_old_files():
    session = transport.open_channel(kind="session")
    session.exec_command('rm -r /home/fpp/media/sequences/*\n\
                    rm -r /home/fpp/media/playlists/*\n\
                    rm -f /home/fpp/media/schedule')
    print("\nOld program deleted!\n")



def generate_playlist():
    f = open(playlist_name, "w+")
    f.write("0,0,\n")
    for sequence in os.listdir():
        if sequence.endswith(".fseq"):
            f.write(f's,{sequence},\n')
    f.close()
    print("Playlist Created!\n")

def generate_schedule():
    f = open("schedule", "w+")
    f.write(schedule)
    f.close
    print("Schedule Created!\n")

def upload_files():
    sequence = 0
    for file in os.listdir():
        if file.endswith(".fseq"):
            sequence += 1
            path = pathlib.PurePosixPath("/home/fpp/media/sequences", file).as_posix()
            local = os.path.join(cwd, file)
            sftp.put(localpath=local, remotepath=path, callback=printTotals)
            # print(f"Sequence {sequence} uploaded\r")
        elif file == playlist_name:
            path = pathlib.PurePosixPath("/home/fpp/media/playlists", file).as_posix()
            local = os.path.join(cwd, file)
            sftp.put(localpath=local, remotepath=path, callback=printTotals)
            # print("Playlist Uploaded\r")
        elif file == "schedule":
            path = pathlib.PurePosixPath("/home/fpp/media", file).as_posix()
            local = os.path.join(cwd, file)
            sftp.put(localpath=local, remotepath=path, callback=printTotals)
            # print("Schedule Uploaded\r")
    sftp.close()
    session = transport.open_channel(kind="session")
    session.exec_command(f'/opt/fpp/bin.pi/fpp -p {playlist_name}')
    transport.close()


def printTotals(transferred, toBeTransferred):
    KB_transferred = transferred * 0.001
    KB_to_be_transferred = toBeTransferred * 0.001
    percentage = transferred / toBeTransferred * 100
    print(f"Transferred: {KB_transferred:.2f}\tOut of: {KB_to_be_transferred:.2f}\t {percentage:.0f}%", end="\r")
    time.sleep(.1)
    
delete_old_files()
generate_playlist()
generate_schedule()
upload_files()

