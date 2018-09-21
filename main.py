import requests
import json

def post_data(data):
    payload = {
    "command": "setInterfaceInfo",
    "data": json.dumps(data)
}
    requests.post("http://fpp.local/fppjson.php", data=payload)

data = {

            "INTERFACE":"",
            "PROTO":"",
            "ADDRESS": "",
            "NETMASK": "",
            "GATEWAY": ""
            
}

def get_data(interface, data):
    if interface == 'wlan0':
        data['SSID'] = input("Enter the WiFi SSID (case sensitive): ")
        data['PSK'] = input("Enter the WiFi password (case sensitive): ")
    for x,y in data.items():
        if x == "INTERFACE":
            print(f"Setting up {interface}\n")
            data[x] = interface
        elif x == "PROTO":
            set_to_static = input("Set IP address to STATIC?(Y/N): ")
            print("\n")
            if set_to_static.lower() == 'y':
                data[x] = 'static'
            else:
                data[x] = 'dhcp'
        elif x == "ADDRESS":
            if data['PROTO'] != 'dhcp':
                if interface == 'eth0':
                    set_ip_address = input(f"Enter an IP address for {interface} (default=192.168.10.1): ")
                    print("\n")
                    if set_ip_address == "":
                        data[x] = "192.168.10.1"
                    else:
                        data[x] = set_ip_address
                else:
                    set_ip_address = input(f"Enter an IP address for {interface} (default=192.168.0.110): ")
                    print("\n")
                    if set_ip_address == "":
                        data[x] = "192.168.0.110"
                    else:
                        data[x] = set_ip_address
        elif x == "NETMASK":
            if data['PROTO'] != 'dhcp':
                data[x] = "255.255.255.0"
        elif x == "GATEWAY" and interface == "wlan0":
            if data['PROTO'] != 'dhcp':
                data[x] = "192.168.0.1"
    print(data)
    return data


#browser.post("http://fpp.local/fppjson.php$command=setInterfaceInfo&data=", json=data)

#eth0_data = get_data("eth0", data)
wlan0_data = get_data("wlan0", data)
#post_data(eth0_data)
post_data(wlan0_data)