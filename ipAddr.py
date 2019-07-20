import paho.mqtt.client as mqtt
import time
import os


if __name__ == "__main__":
    host = "MTL-700-NOA55.MTL1.CO.TH"
    port = 1883
    client = mqtt.Client("Rasp1")
    client.connect(host)

    f = os.popen('ifconfig wlan0 | grep "inet 163" | cut -c 14-26')
    myip=f.read()
    print(myip)

    while True:
        client.loop_start()
        client.publish("ipAddr/Rasp/NPMSA414", str(myip))
        time.sleep(60)
        client.loop_stop()
