import time
from multiprocessing import Process, Lock

class DependencyFactory:

	services = {}
	started_services = []
	lock = Lock()
	
	@staticmethod
	def get(name):
		return DependencyFactory.services[name]

	def start(name):
		if name in DependencyFactory.started_services:
				return True
		print("Starting Service {0}".format(name))
		time.sleep(3)
		print("Service {0} started".format(name))
		if name in DependencyFactory.started_services:
				return True
		DependencyFactory.started_services.append(name)

	def stop(name):
		try:
			DependencyFactory.started_services.pop(name)
		except:
			pass
		print("Stoping Service {0}".format(name))
		time.sleep(2)
		print("Service {0} stopped".format(name))
		


