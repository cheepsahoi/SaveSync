# Get WiFI SSID
import subprocess

def getSystemOS():
    try:
        subprocess.run(["ls"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        os = "linux"
        print("Linux/MacOS detected.")
    except FileNotFoundError:
        os = "windows"
        print("Windows detected.")
    return os

# Get SSID for specified System OS
def WifiSSID(SystemOS):
    # For Linux/MacOS
    if SystemOS == "linux":
        output = subprocess.check_output(["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"])
        output = output.decode("utf-8")
        for line in output.split("\n"):
            if "SSID: " in line:
                ssid = line.split(": ")[1]
                print(ssid)
    # For Windows OS
    elif SystemOS == "windows":
        print("subprocess imported")
        output = subprocess.check_output(["netsh", "wlan", "show", "interfaces"])
        print("First output")
        output = output.decode("utf-8")
        print("Second output")

        for line in output.split("\n"):
            if "SSID" in line:
                ssid = line.split(":")[1].strip()
                print(ssid)

        # import wlanapi
        # print("wlanapi imported. Press enter.")
        # wlan = wlanapi.WLANAPI()
        # interface_guid = wlan.get_interface_guid()
        # current_network = wlan.get_current_network(interface_guid)
        # ssid = current_network.get("ssid")


WifiSSID(getSystemOS())
input("Press enter to exit.")