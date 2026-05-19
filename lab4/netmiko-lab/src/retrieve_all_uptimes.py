from netmiko import Netmiko

# List of all routers
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

# Loop through all routers
for device in devices:

    print("-" * 60)

    # Connect to router
    net_connect = Netmiko(**device)

    # Run show version command
    output = net_connect.send_command("show version")

    # Disconnect from router
    net_connect.disconnect()

    # Find uptime text
    result = output.find("uptime is")

    # Extract uptime information
    begin = int(result)
    end = begin + 50

    # Print uptime
    print(f"Router IP: {device['ip']}")
    print(output[begin:end])

print("-" * 60)
print("Finished collecting uptimes")
