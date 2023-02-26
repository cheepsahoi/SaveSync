# Get WiFI SSID
SystemOS = prompt("What OS? MacOS (M) or Windows (W)? : ")

# Get SSID for specified System OS
def WifiSSID(SystemOS):
    # For MacOS
    if SystemOS.lower() == "m":
        import subprocess
        output = subprocess.check_output(["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"])
        output = output.decode("utf-8")

        for line in output.split("\n"):
            if "SSID: " in line:
                ssid = line.split(": ")[1]
                print(ssid)
    # For Windows OS
    elif SystemOS.lower() == "l":
        import wlanapi
        wlan = wlanapi.WLANAPI()
        interface_guid = wlan.get_interface_guid()
        current_network = wlan.get_current_network(interface_guid)
        ssid = current_network.get("ssid")

WifiSSID()
