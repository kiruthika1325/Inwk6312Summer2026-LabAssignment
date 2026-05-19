from netmiko import Netmiko

# List of all routers/devices
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.104",
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    }
]

# Loop through each device
for device in devices:

    print("-" * 50)

    # Connect to router
    net_connect = Netmiko(**device)

    # Enter enable mode
    net_connect.enable()

    # Get router prompt
    prompt = net_connect.find_prompt()

    # Print device IP and prompt
    print(f"Connected to: {device['ip']}")
    print(f"Router Prompt: {prompt}")

    # Disconnect session
    net_connect.disconnect()

print("-" * 50)
print("Completed Successfully")
