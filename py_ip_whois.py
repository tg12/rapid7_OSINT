'''THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND
NON-INFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR ANYONE
DISTRIBUTING THE SOFTWARE BE LIABLE FOR ANY DAMAGES OR OTHER LIABILITY,
WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

# Bitcoin Cash (BCH)   qpz32c4lg7x7lnk9jg6qg7s4uavdce89myax5v5nuk
# Ether (ETH) -        0x843d3DEC2A4705BD4f45F674F641cE2D0022c9FB
# Litecoin (LTC) -     Lfk5y4F7KZa9oRxpazETwjQnHszEPvqPvu
# Bitcoin (BTC) -      34L8qWiQyKr8k4TnHDacfjbaSqQASbBtTd

# contact :- github@jamessawyer.co.uk



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

