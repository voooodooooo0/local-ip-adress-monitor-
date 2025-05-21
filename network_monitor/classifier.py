from mac_vendor_lookup import MacLookup

mac_lookup = MacLookup()
# mac_lookup.update_vendors()  # Uncomment only if you want to update the database

def classify(mac):
    try:
        vendor = mac_lookup.lookup(mac).lower()
        # Device type
        if "apple" in vendor or "samsung" in vendor:
            device_type = "Phone"
        elif "intel" in vendor or "dell" in vendor or "hp" in vendor or "amd" in vendor:
            device_type = "Computer"
        else:
            device_type = "Other"
        # OS guess
        if "apple" in vendor:
            os_guess = "iOS/macOS"
        elif "samsung" in vendor:
            os_guess = "Android"
        elif "intel" in vendor or "amd" in vendor:
            os_guess = "Computer OS"
        else:
            os_guess = "Unknown"
        return device_type, os_guess
    except:
        return "Unknown", "Unknown"
