import yaml
from service import Service
from service_manager import ServiceManager



def load_config():
	print("Loading config.yaml")
	with open("config.yaml") as f:
		return yaml.load(f)

def get_services(configs):
	services = []
	for service, dependencies in configs.items():
		dependencies = dependencies.get('deps', [])
		services.append(Service(service, dependencies))

	for service in services:
		service.add_dependencies()

	for service in services:
		service.add_reverse_dependencies()

	for service in services:
		print(service)
	return services

def start_program(manager):	
	while True:
		print("Select any option to start/stop the services ")
		print("1: start")
		print("2: stop")
		print("3: exit")
		option = input("Enter the option ")
		if option.lower() in ['start', '1']:
			print("Starting the services")
			manager.start_services()
		elif option.lower() in ['stop', '2']:
			manager.stop_services()
			print("Stoping the services")
		elif option.lower() in ['exit', '3']:
			print("Exiting the Program")
			exit()


if __name__ == '__main__': 
	print("Starting Program")
	configs = load_config()
	manager = ServiceManager(get_services(configs))
	start_program(manager)

