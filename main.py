import requests
import json
from tkinter import *

    
class App:

    def __init__(self, master):

        first_frame = Frame(master, pady=5, padx=5)
        second_frame = Frame(master, pady=5, )
        third_frame = Frame(master, pady=5, )
        fourth_frame = Frame(master, pady=5, )
        first_frame.pack()
        second_frame.pack()
        third_frame.pack()
        fourth_frame.pack()

        self.button = Button(fourth_frame, text="Quit", fg="red", command=fourth_frame.quit)
        self.button.pack(side=RIGHT)

        self.save_button = Button(fourth_frame, text="Save", command=self.save)
        self.save_button.pack(side=LEFT)

        self.ip_address = Label(first_frame, text="Enter new IP address: ")
        self.ip_address.pack(SIDE=LEFT)
        self.address = Entry(first_frame, text="New IP")
        self.address.pack()

        self.name_var = StringVar()
        self.name = Entry(second_frame, textvariable=self.name_var)
        self.name.pack()


    def save(self):
        var = self.name_var.get()
        if var == "":
            print("Invalid Input")
        else:
            print("Updated")
            post_data()

       


data = {

            "INTERFACE":"eth0",
            "PROTO":"static",
            "ADDRESS": "192.168.0.1",
            "NETMASK": "255.255.255.0",
            "GATEWAY": "192.168.0.1"
            
}

payload = {
    "command": "setInterfaceInfo",
    "data": json.dumps(data)
}
# # browser.post("http://fpp.local/fppjson.php$command=setInterfaceInfo&data=", json=data)
def post_data():
    r = requests.post("http://fpp.local/fppjson.php", data=payload)

root = Tk()

app = App(root)
root.mainloop()