import urequests as requests
import network
from time import sleep


ssid = 'ssid'
password = 'password'

#   Connect to local WLAN
def connect_Wifi():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
 #   print(wlan.ifconfig())
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

#   Get Myip from no-ip.com
def change_ip(Myip):
#   My account at no-ip.com    
    username = "username"
    password = "password"
    hostname = "hostname"
#   prepare Myip  as e.g "90.143.155.160"        
    ipst = str(Myip)
    ipst = ipst.rstrip()  # strip spaces in ipst
    Myip = '"' + ipst +'"'

    print('change IP=' , Myip)

    url = f"https://dynupdate.no-ip.com/nic/update?hostname={hostname}&myip={Myip}"

    response = requests.get(url, auth=(username, password))

    print(response.text)
    return


# Main Program

connect_Wifi()

x = requests.get("http://wtfismyip.com/text").text

print('My router IP is: ', x)
new_ip = str(x)

file_old = open("old_ip.txt", "r")
old_ip = file_old.read()
print ('old_IP =', old_ip)
file_old.close()

print('new_ip =',new_ip)
if old_ip != new_ip:
    file = open("old_ip.txt", "w")
    file.write(new_ip)
    file.close()
    change_ip(new_ip)
    
else:
     print('No change')
     


    
