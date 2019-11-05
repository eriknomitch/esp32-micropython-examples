from umqtt import MQTTClient
from machine import Pin
import ubinascii
import machine
import micropython
import ujson
import utime as time

import graph
import ssd1306

# ------------------------------------------------
# CONSTANTS --------------------------------------
# ------------------------------------------------
OLED_X = 128
OLED_Y = 64
SERVER = "192.168.1.10"
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
TOPIC = b"rain-graph"

GRAPH_WIDTH = 120
GRAPH_HEIGHT = 60
GRAPH_Y = 15
GRAPH_X = 100

# ------------------------------------------------
# GLOBALS ----------------------------------------
# ------------------------------------------------
i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(OLED_X, OLED_Y, i2c)
graph = graph.Graph(oled)

# ------------------------------------------------
# MQTT -------------------------------------------
# ------------------------------------------------
def sub_cb(topic, msg):
    print((topic, msg))
    print(ujson.loads(msg))

    graph.clear()

    try:

        if all(precipitation == 0 for precipitation in ujson.loads(msg)["rain"]):
            oled.text("No rain.", 0, 0)
            oled.show()
        else:
            i = 1
            for precipitation in ujson.loads(msg)["rain"]:
                graph.draw_bar(i, precipitation)
                i = i + 1
    except:
        oled.text("Error", 0, 0)
        oled.show()

# ------------------------------------------------
# MAIN -------------------------------------------
# ------------------------------------------------
def main(server=SERVER):

    c = MQTTClient(CLIENT_ID, server)

    #Subscribed messages will be delivered to this callback
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(TOPIC)
    print("Connected to %s, subscribed to %s topic" % (server, TOPIC))

    oled.text("connected.", 0, 20)
    oled.show()

    try:
       while 1:
           #micropython.mem_info()
           c.wait_msg()
    finally:
       c.disconnect()


# ================================================
# MAIN ===========================================
# ================================================
main()
