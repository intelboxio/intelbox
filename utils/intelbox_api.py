from utils.singleton import singleton
from utils import net_op
import config, base64, json

@singleton
class intelbox_api():
	def __init__(self):
		pass
		
	def upload_sample(self, filename, filepath, run_time = 60):
		data = {
			"run_time": run_time
		}
		files = {
			'file' : (filename, open(filepath, 'rb'))
		}
		
		return net_op.request_post("{}/v2/file/upload?apikey={}".format(config.API_SERVER, config.API_KEY), data, files)
		
	def upload_pcap(self, filename, filepath):
		files = {
			'file' : (filename, open(filepath, 'rb'))
		}
		
		return net_op.request_post("{}/v2/pcap/upload?apikey={}".format(config.API_SERVER, config.API_KEY), {}, files)

	def fetch_ipv4(self, ipv4, relationship):
		return net_op.request_get("{}/v2/ip/report?apikey={}&ip={}&relationship={}".format(config.API_SERVER, config.API_KEY, ipv4, relationship))
		
	def fetch_domain(self, domain, relationship):
		return net_op.request_get("{}/v2/domain/report?apikey={}&domain={}&relationship={}".format(config.API_SERVER, config.API_KEY, domain, relationship))

	def fetch_hash(self, file_hash, relationship):
		return net_op.request_get("{}/v2/file/report?apikey={}&file_hash={}&relationship={}".format(config.API_SERVER, config.API_KEY, file_hash, relationship))
		
	def submit_query(self, keyword, page = 1):
		return net_op.request_get("{}/v2/advanced/keywords?apikey={}&key_word={}&page={}".format(config.API_SERVER, config.API_KEY, keyword, page))

	def submit_url(self, obj):
		return net_op.request_post("{}/v2/submit/url".format(config.API_SERVER), obj)