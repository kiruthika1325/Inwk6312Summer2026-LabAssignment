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

# Loop through routers
for device in devices:

    print("\n" + "=" * 70)
    print(f"Router: {device['ip']}")
    print("=" * 70)

    # Connect to router
    net_connect = Netmiko(**device)

    # Execute command using TextFSM
    output = net_connect.send_command(
        "show ip interface brief",
        use_textfsm=True
    )

    # Disconnect
    net_connect.disconnect()

    # Print all interfaces
    for interface in output:

        print(f"Interface Name : {interface['interface']}")
        print(f"IP Address     : {interface['ip_address']}")
        print(f"Status         : {interface['status']}")
        print(f"Protocol       : {interface['proto']}")
        print("-" * 40)

print("\nFinished collecting interface information")
