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

# Loop through all routers
for device in devices:

    print("\n" + "=" * 80)
    print(f"Router: {device['ip']}")
    print("=" * 80)

    # Connect to router
    net_connect = Netmiko(**device)

    # Run command using TextFSM
    output = net_connect.send_command(
        "show ip route",
        use_textfsm=True
    )

    # Disconnect from router
    net_connect.disconnect()

    # Loop through routing table entries
    for route in output:

        print(f"Protocol : {route['protocol']}")
        print(f"Network  : {route['network']}")
        print(f"Distance : {route['distance']}")
        print(f"Metric   : {route['metric']}")
        print("-" * 50)

print("\nFinished parsing routing tables")
