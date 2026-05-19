from netmiko import ConnectHandler

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

    print("=" * 70)
    print(f"Connecting to Router: {device['ip']}")
    print("=" * 70)

    # Connect to router
    net_connect = ConnectHandler(**device)

    # Execute command
    output = net_connect.send_command("show interface description")

    # Print output
    print(output)

    # Disconnect
    net_connect.disconnect()

print("=" * 70)
print("Completed Successfully")
