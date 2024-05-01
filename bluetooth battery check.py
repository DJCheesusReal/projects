import pygatt

def get_battery_level(device_address):
    try:
        adapter = pygatt.GATTToolBackend()

        adapter.start()
        device = adapter.connect(device_address)

        # Read battery level characteristic
        battery_level = device.char_read("00002a19-0000-1000-8000-00805f9b34fb")
        print(f'Battery level of {device_address}: {int(battery_level[0])}%')

        device.disconnect()
        adapter.stop()
    except Exception as e:
        print(f'Error retrieving battery level for {device_address}: {e}')

def main():
    adapter = pygatt.GATTToolBackend()

    adapter.start()
    devices = adapter.scan(run_as_root=True)

    print("Scanning for nearby Bluetooth devices...")
    for address, name in devices.items():
        print(f"Found device: {name} ({address})")
        get_battery_level(address)

    adapter.stop()

if __name__ == "__main__":
    main()
