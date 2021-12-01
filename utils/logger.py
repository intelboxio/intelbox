from utils.singleton import singleton
from utils import color

@singleton
class Logger(object):
	def __init__(self):
		pass

	def nothing(self):
		print("")

	def info(self, s):
		print(s)
	
	def title(self, key, value):
		print("{} {} of {}".format(color.colorize("[!]", "blue"), color.colorize(key, "green"), color.colorize(value, "lightyellow")))

	def query_title(self, key, value):
		print("{} {} : {}".format(color.colorize("[!]", "blue"), color.colorize(key, "green"), color.colorize(value, "lightyellow")))

	def ip_format(self, key, value):
		print("{} {} : {}".format(color.colorize("[+]", "blue"), key, color.colorize(value, "lightyellow")))

	def domain_format(self, value):
		print("{} {}".format(color.colorize("[+]", "blue"), color.colorize(value, "lightyellow")))	

	def query_format(self, key, value):
		print("{} {} is {}".format(color.colorize("[+]", "blue"), color.colorize(key, "green"), color.colorize(value, "lightyellow")))	

	def debug(self, s):
		print(color.colorize(s, "blue"))

	def error(self, s):
		print("[!] {}".format(color.colorize(s, "red")))