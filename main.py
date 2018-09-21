import requests
import json
from tkinter import *

data = {

            "INTERFACE":"eth0",
            "PROTO":"static",
            "ADDRESS": "192.168.0.1",
            "NETMASK": "255.255.255.0",
            "GATEWAY": "192.168.0.1"
            
}


class AddressInputForm :
    def __init__(self) :
        self.root = None
        self.nameentry = None
        self.name = ""
        self.address = ""

    def CloseWindow(self) :
        self.name = self.nameentry.get()
        self.address = self.addressentry.get()
        self.root.destroy()

    def CreateForm(self) :
        self.root = Tk()
        self.root.title("Control Updater")
        Label(self.root, text="Enter IP address 192.168.").grid(row=0, sticky=W)
        Label(self.root, text=".").grid(row=0, column=2)
        Label(self.root, text="Enter address:").grid(row=1, sticky=W)

        self.nameentry = Entry(self.root, width=5, justify=LEFT)
        self.addressentry = Entry(self.root)

        self.nameentry.grid(row=0, column=1)
        self.addressentry.grid(row=1, column=1)

        Button(self.root, text="Ok", command=self.CloseWindow).grid(row=2,column=0)
        Button(self.root, text="Cancel", command=self.CloseWindow).grid(row=2, column=1)
        self.root.mainloop()

af = AddressInputForm()
af.CreateForm()


       




# payload = {
#     "command": "setInterfaceInfo",
#     "data": json.dumps(data)
# }
# # # browser.post("http://fpp.local/fppjson.php$command=setInterfaceInfo&data=", json=data)
# def post_data():
#     r = requests.post("http://fpp.local/fppjson.php", data=payload)
