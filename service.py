import time
from dependency_factory import DependencyFactory

class Service:

	def __init__(self, name, dependencies):
		self.name = name
		self.started = False
		self.dependencies = dependencies
		DependencyFactory.services[name] = self
		self.reverse_dependencies_objects = []

	def add_dependencies(self):
		self.dependencies_objects = []
		for dependency in self.dependencies:
			self.dependencies_objects.append(DependencyFactory.get(dependency))

	def add_reverse_dependencies(self):
		
		for dependency in self.dependencies_objects:
			dependency.reverse_dependencies_objects.append(DependencyFactory.get(self.name))


	def is_started(self):
		return self.started

	def start_dependencies(self):
		for dependency in self.dependencies_objects:
			dependency.start()

	def stop_dependencies(self):
		for dependency in self.reverse_dependencies_objects:
			dependency.stop()


	def start(self):
		try:
			self.start_dependencies()
			if self.name in DependencyFactory.started_services:
				print("Service {0} is already started".format(self.name))
				return True
			DependencyFactory.start(self.name)
				
		except Exception as e:
			print("Service {0} cannot be started ".format(self.name))

	def stop(self):
		try:
			self.stop_dependencies()
			if self.name not in DependencyFactory.started_services:
				print("Service {0} is already stopped".format(self.name))
				return True
			DependencyFactory.stop(self.name)
		except Exception as e:
			print("Service {0} cannot be stopped ".format(self.name))
		

	def __str__(self):
		deps = [ str(deps) for deps in self.dependencies]
		return "Serivce {0} with Dependency [{1}] ".format(self.name, deps)



