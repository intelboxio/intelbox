<p align="center">
  <p align="center">
    <a href="https://github.com/intelboxio/intelbox"><img alt="python" src="https://img.shields.io/badge/python-3.6%2B-blue.svg"></a>
    <a href=""><img alt="Software License" src="https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square"></a>
    <a href="https://github.com/intelboxio/intelbox"><img alt="Release" src="https://img.shields.io/badge/version-1.0.0-red.svg"></a>
  </p>
</p>

# What is Intelbox?

Intelbox is an intelligence threat shared platform, which allows security researcher to analyze suspicious files, IP and domains to detect types of cyber threats.

# How to use
If you have no idea what are you doing just type the command below
```
./intelbox.py --help

usage: intelbox.py [-h] [-o OUTPUT] {domain,ip,hash} ...

positional arguments:
  {domain,ip,hash}  Commands
    domain          Domain relative information
    ip              IP relative information
    hash            File hash relative information

optional arguments:
  -h, --help        show this help message and exit
  -o OUTPUT         Output result in json format to the given filename

[*] Example command
./intelbox.py ip 8.8.8.8 services
./intelbox.py domain google.com engines
./intelbox.py hash b10e280dc300f75475323539cc6b645b engines
./intelbox.py query "port=7001&&product=weblogic"
```

# Advanced query usage supported
- [x] "port==443"
- [x] "title=weblogic"
- [x] "protocol=https"
- [x] "product=jboss"
- [x] "city=Chiyoda"
- [x] "country=Japan"
- [x] "countryCode=JP"
- [x] "isp!=SOFTBANK Corp"
- [x] "org=Japan nation-wide Network of SOFTBANK Corp."
- [x] "regionName=Tokyo"
- [x] "port=7001&&product=weblogic"
- [x] "port=7001||product=weblogic"

# Contact
intelboxio@protonmail.com

# Disclaimer
This tool is for educational purposes only. You are responsible for your own actions. If you mess something up or break any laws while using this software, it's your fault, and your fault only.

# Contribute
If you have some new idea about this project or you have found some valuable tool feel free to open an issue