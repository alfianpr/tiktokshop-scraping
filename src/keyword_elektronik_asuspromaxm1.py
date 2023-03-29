import time
from utils_keyword import open_product_v1_search_asuspromaxm1, open_product_v2_search_asuspromaxm1, driver, close_dialog

# Setup Connection and product
SCROLL_LOOP = 100
CATEGORY = "Elektronik"
CONNECTION = "192.168.0.101:5555"
SKIP = False  # First time set to False, set True if you want to continue the process
SERVER_APPIUM_PORT = "4723"
SERVER_APPIUM_IP = "127.0.0.1"

DESIRED_CAPS = {
    "platformName": "Android",
    "deviceName": "device",
    "udid": CONNECTION,
    "noReset": True,
}

driver = driver(SERVER_APPIUM_IP=SERVER_APPIUM_IP, SERVER_APPIUM_PORT=SERVER_APPIUM_PORT, desired_caps=DESIRED_CAPS)

### Scroll Default
startx = driver.get_window_size()['width']*1/4; endx = driver.get_window_size()['width']*1/4
starty = driver.get_window_size()['height']*8/11; endy = driver.get_window_size()['height']/8

k = 0
while k <= SCROLL_LOOP:
    print (f"Scrape the loop at {k}")
    time.sleep(2); open_product_v2_search_asuspromaxm1(CATEGORY=CATEGORY, SKIP=SKIP, k=k)
    driver.swipe(startx, 1900, endx, 850, 200) # Adjust with your device
    time.sleep(2)
    try: close_dialog()
    except: pass
    k = k + 1