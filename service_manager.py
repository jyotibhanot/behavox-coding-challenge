from concurrent.futures import ThreadPoolExecutor
import threading
import random
from time import time


class ServiceManager:

	def __init__(self, services):
		self.services = services
		self.flag = False
		self.executor = ThreadPoolExecutor(max_workers=5)

	def start_services(self):
		for service in self.services:
			#self.service_pool.apply_async(service.start, ())
			self.executor.submit(service.start)
	def stop_services(self):
		for service in self.services:
			#self.service_pool.apply_async(service.stop, ())
			self.executor.submit(service.stop)







