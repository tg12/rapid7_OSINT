from ipwhois import IPWhois
import requests
import re
# from concurrent.futures import ThreadPoolExecutor
from random import randint
from time import sleep

response = requests.get(
    "https://raw.githubusercontent.com/tg12/rapid7_OSINT/master/osint_data.txt")
ips = []

regex = re.findall(
    r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})', str(
        response.text))
if regex is not None:
    for match in regex:
        if match not in ips:
            ips.append(match)


def check_whois(ip):
    obj = IPWhois(ip)
    result = obj.lookup_rdap(depth=1)
    # print (result) #debug
    print("[+]debug : " + str(ip))
    print("[+]debug : " + str(result['asn_description']))
    print("########")
    return str(result['network']['name'])


i = 0
for each in ips:
    try:
        i += 1
        # print ("still working...." + str(i))
        sleep(randint(1, 3))
        check_whois(each)
    except BaseException:
        pass

# http 429, too fast!!
# with ThreadPoolExecutor(max_workers=100) as pool:
        # pool.map(check_whois, ips)

