from netmiko import ConnectHandler

# Router list
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

# List of show commands
commands = [
    "show ip interface brief",
    "show version",
    "show ip route",
    "show cdp neighbors"
]

# Loop through routers
for device in devices:

    print("\n" + "=" * 80)
    print(f"Connected to Router: {device['ip']}")
    print("=" * 80)

    # Connect to router
    net_connect = ConnectHandler(**device)

    # Run each command
    for command in commands:

        print("\n" + "-" * 60)
        print(f"COMMAND: {command}")
        print("-" * 60)

        output = net_connect.send_command(command)

        print(output)

    # Disconnect
    net_connect.disconnect()

print("\nFinished executing all commands")
