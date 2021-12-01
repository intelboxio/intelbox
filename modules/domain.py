from utils.singleton import singleton
from utils.intelbox_api import intelbox_api
from utils.logger import Logger
import json

@singleton
class domain_module():
	def __init__(self):
		pass
		
	def do(self, domain, options):
		Logger().debug("Response:")
		data = intelbox_api().fetch_domain(domain, options.relationship)
		
		if data:
			if data["code"] == 0:
				if options.output:
					with open(options.output, 'w') as outfile:
						json.dump(data["data"], outfile, indent=2)
						print("Save to file: {}".format(options.output))
				else:
					print(json.dumps(data["data"], indent=2, sort_keys=True))
			else:
				Logger().error(data["msg"])
		else:
			Logger().error("Something error")