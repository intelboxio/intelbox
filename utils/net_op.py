from http.client import HTTPSConnection
import struct, socket, psutil, ipaddress
import urllib.parse
import requests, json

def request_common(method, url, json, files):
	try:
		r = method(url, json = json, files = files, timeout = 60)

		if r.status_code == 200:
			return r.json()
	except Exception as e:
		print(e)
	
	return None
	
def request_get(url, json = None):
	return request_common(requests.get, url, json, None)
	
def request_post(url, json = None, files = None):
	return request_common(requests.post, url, json, files)

def request_head(url):
	try:
		r = requests.head(url, timeout = 3)
		
		return json.dumps(dict(r.headers))
	except Exception as e:
		pass

	return None