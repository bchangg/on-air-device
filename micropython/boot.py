import gc

import config
import esp

import micropython

esp.osdebug(None)
gc.collect()


def do_connect():
    import network

    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print("connecting to network...")
        wlan.active(True)
        wlan.connect(config.WIFI_SSID, config.WIFI_PASSWORD)
        while not wlan.isconnected():
            pass
    print("network config:", wlan.ifconfig())


do_connect()
