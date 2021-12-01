#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse, sys, textwrap
from utils.logger import Logger
from modules.ipv4 import ipv4_module
from modules.domain import domain_module
from modules.hash import hash_module
from modules.query import query_module

version = "1.1.0"

def banner():
	banner = """
  _____       _       _ _               
 |_   _|     | |     | | |              
   | |  _ __ | |_ ___| | |__   _____  __
   | | | '_ \| __/ _ \ | '_ \ / _ \ \/ /
  _| |_| | | | ||  __/ | |_) | (_) >  < 
 |_____|_| |_|\__\___|_|_.__/ \___/_/\_\ \n"""
	
	Logger().info(banner)
	Logger().info("An intelligence gathering client, which communicating with api.intelbox.io")
	Logger().nothing()

"""
	Usage:
		Command:
			intelbox whois baidu.com
"""
if __name__ == "__main__":
	banner()

	parser = argparse.ArgumentParser(
		formatter_class = argparse.RawDescriptionHelpFormatter,
		# epilog = textwrap.dedent('''\
		# 	Advanced query syntax supported:
		# 		"port==443"
		# 		"title=weblogic"
		# 		"protocol=https"
		# 		"product=jboss"
		# 		"city=Chiyoda"
		# 		"country=Japan"
		# 		"countryCode=JP"
		# 		"isp!=SOFTBANK Corp"
		# 		"org=Japan nation-wide Network of SOFTBANK Corp."
		# 		"regionName=Tokyo"
		# 		"port=7001&&product=weblogic"
		# 		"port=7001||product=weblogic"
		# '''
		# )
	)
	
	#/v1/advanced/keywords?apikey=bRMQ4U47U2lYrsWrpTOki1BbJTHuLjZd&key_word=port=7001&&product=weblogic&page=1
	#/v1/advanced/keywords?apikey=bRMQ4U47U2lYrsWrpTOki1BbJTHuLjZd&key_word=port%3D7001%26%26product%3Dweblogic
	parser.add_argument('-o', action = "store", dest='output', help = 'Output result in json format to the given filename')
	subparsers = parser.add_subparsers(help = 'Commands')
	
	#Domain command
	domain_parser = subparsers.add_parser('domain', help = 'Domain relative information')
	domain_parser.add_argument('domain_value', action = 'store', help = 'Domain name')
	domain_parser.add_argument('relationship', choices=['engines', 'communicating_files', 'historical_ssl_certificates', 'historical_whois', 
								'referrer_files', 'resolutions', 'parent', 'siblings', 'subdomains'])

	#IPv4 command
	ipv4_parser = subparsers.add_parser('ip', help = 'IP relative information')
	ipv4_parser.add_argument('ipv4_value', action = 'store', help = 'IPv4 address')
	ipv4_parser.add_argument('relationship', choices=['engines', 'geo', 'communicating_files', 'historical_ssl_certificates', 'historical_whois', 
								'referrer_files', 'resolutions', 'services', 'vulns'])

	#hash command
	hash_parser = subparsers.add_parser('hash', help = 'File hash relative information')
	hash_parser.add_argument('hash_value', action = 'store', help = 'MD5, SHA-1, SHA-256')
	hash_parser.add_argument('relationship', choices=['engines', 'contacted_domains', 'contacted_urls', 'contacted_ips', 'behaviours', 
								'pe_resource_parents', 'execution_parents', 'bundled_files', 'dropped_files', 'pe_resource_children'])
	
	#Query command
	# query_parser = subparsers.add_parser('query', help = 'Advanced query')
	# query_parser.add_argument('--page', action = "store", default = 1, help = 'Page number to query, default 1')
	# query_parser.add_argument('keyword', action = 'store', help = 'Keyword to query')

	args = parser.parse_args()
	
	if "ipv4_value" in args:
		ipv4_module().do(args.ipv4_value, args)	
	elif "domain_value" in args:
		domain_module().do(args.domain_value, args)
	elif "hash_value" in args:
		hash_module().do(args.hash_value, args)
	elif "keyword" in args:
		query_module().do(args.keyword, args)
	else:
		parser.print_help()