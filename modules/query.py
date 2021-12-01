from utils.singleton import singleton
from utils.intelbox_api import intelbox_api
from utils import net_op
from utils.logger import Logger
import config, base64, json
import urllib.parse

@singleton
class query_module():
	def __init__(self):
		pass

	def do(self, keyword, options):
		Logger().query_format("Keyword", keyword)
		Logger().query_format("Selected page", options.page)
		Logger().nothing()

		keyword = urllib.parse.quote(keyword)
		data = intelbox_api().submit_query(keyword, options.page)
		
		if data:
			if data["code"] == 0:
				Logger().query_title("Found results", data["data"]["length"])
				Logger().query_title("Limit results of single page", data["data"]["limit"])
				Logger().query_title("Current page", data["data"]["page"])
				Logger().info(json.dumps(data["data"]["data"], indent = 2))

				if options.output:
					with open(options.output, 'w') as outfile:
						json.dump(data["data"]["data"], outfile, indent = 2)
			else:
				Logger().error(data["msg"])
		else:
			Logger().error("Something error")