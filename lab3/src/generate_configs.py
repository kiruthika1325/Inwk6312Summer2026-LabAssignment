from jinja2 import Environment, FileSystemLoader
import yaml

# Load Jinja template environment
env = Environment(loader=FileSystemLoader('.'))

# Load template
template = env.get_template("router_template.j2")

# Load YAML data
with open("routers.yml") as file:
    data = yaml.safe_load(file)

# Generate configuration for each router
for router in data["routers"]:

    config = template.render(router=router)

    filename = f"{router['hostname']}_config.txt"

    with open(filename, "w") as output_file:
        output_file.write(config)

    print(f"{filename} generated successfully.")
