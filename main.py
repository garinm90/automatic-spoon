import requests
import json
from tkinter import *

    
class App:

    def __init__(self, master):

        frame = Frame(master, pady=5, padx=5)
        bottom_frame = Frame(master, pady=5, )
        frame.pack()
        bottom_frame.pack()

        self.button = Button(
            frame, text="Quit", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Save", command=self.save)
        self.hi_there.pack(side=LEFT)

        self.address = Entry(
            frame, text="New IP"
        )
        self.address.pack()

        self.name_var = StringVar()
        self.name = Entry(bottom_frame, textvariable=self.name_var)
        self.name.pack()


    def save(self):
        var = self.name_var.get()
        if var == "":
            print("Invalid Input")
        else:
            print(var)

       

root = Tk()

app = App(root)
root.mainloop()
# data = {

#             "INTERFACE":"eth0",
#             "PROTO":"static",
#             "ADDRESS": "192.168.0.1",
#             "NETMASK": "255.255.255.0",
#             "GATEWAY": "192.168.0.1"
            
# }

# payload = {
#     "command": "setInterfaceInfo",
#     "data": json.dumps(data)
# }
# # browser.post("http://fpp.local/fppjson.php$command=setInterfaceInfo&data=", json=data)
# r = requests.post("http://fpp.local/fppjson.php", data=payload)
