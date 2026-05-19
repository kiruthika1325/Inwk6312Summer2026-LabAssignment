from netmiko import Netmiko

# List of routers
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.104",
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    }
]

# Loop through routers
for device in devices:

    print("-" * 60)

    # Connect to router
    net_connect = Netmiko(**device)

    # Run command
    output = net_connect.send_command("show version")

    # Disconnect
    net_connect.disconnect()

    # Find configuration register line
    result = output.find("Configuration register is")

    # Extract config register information
    begin = int(result)
    end = begin + 40

    # Print output
    print(f"Router IP: {device['ip']}")
    print(output[begin:end])

print("-" * 60)
print("Finished collecting configuration registers")
