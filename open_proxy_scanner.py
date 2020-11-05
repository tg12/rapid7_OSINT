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



# I am not affiliated, associated, authorized, endorsed by, or in any way officially connected with rapid7.com, or any of its subsidiaries or its affiliates.
# https://opendata.rapid7.com/sonar.http/
# https://github.com/rapid7/sonar/wiki/HTTP

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND
# NON-INFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR ANYONE
# DISTRIBUTING THE SOFTWARE BE LIABLE FOR ANY DAMAGES OR OTHER LIABILITY,
# WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Could use some help to rent a bigger VPS to get the bigger datasets!
# Bitcoin Cash (BCH)   qpz32c4lg7x7lnk9jg6qg7s4uavdce89myax5v5nuk
# Ether (ETH) -        0x843d3DEC2A4705BD4f45F674F641cE2D0022c9FB
# Litecoin (LTC) -     Lfk5y4F7KZa9oRxpazETwjQnHszEPvqPvu
# Bitcoin (BTC) -      34L8qWiQyKr8k4TnHDacfjbaSqQASbBtTd

import json
import gzip
import base64
import csv
import glob
import re
import pandas as pd
from fake_useragent import UserAgent
import requests
from concurrent.futures import ThreadPoolExecutor
import random
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ua = UserAgent()
check_ip = [
    "https://ifconfig.me/ip",
    "https://www.myexternalip.com/raw",
    "http://ipecho.net/plain"]

http_proxy = ""
https_proxy = ""
ftp_proxy = ""

OUTFILE = "outfile.csv"

bypass_err = [
    "404 Not Found",
    "403 Forbidden",
    "403",
    "404",
    "ERROR: The requested URL could not be retrieved",
    "400 Bad Request",
    "Not Found",
    "Moved Permanently",
    "Unauthorized",
    "401 Authorization Required",
    "502 Bad Gateway",
    "407 Proxy Authentication Required",
    "Access Denied",
    "Document moved",
    "Bad Request",
    "400 The plain HTTP request was sent to HTTPS port",
    "401",
    "503",
    "ERROR: Forbidden",
    "Error"
]

header_section_re = re.compile(
    r'HTTP/(?P<version>\d+\.?\d*) (?P<status>\d+ .+?)((\r\n)|(\n))(?P<headers>.+?)((\r\n\r\n)|(\n\n))',
    flags=re.DOTALL)
header_re = re.compile('(?P<name>.+?): (?P<value>.+)(\r?)')
title_re = re.compile(
    r'(\<title\>)(?P<title>.+?)(\</title\>)',
    flags=re.IGNORECASE)
server_re = re.compile('Server: (?P<server>.+?)\r?\n', flags=re.IGNORECASE)
content_type_re = re.compile(
    'Content-Type: (?P<content_type>.+?)\r?\n',
    flags=re.IGNORECASE)
content_encoding_re = re.compile(
    'Content-Encoding: (?P<content_encoding>.+?)\r?\n',
    flags=re.IGNORECASE)
last_modified_re = re.compile(
    'Last-Modified: (?P<last_modified>.+?)\r?\n',
    flags=re.IGNORECASE)
x_powered_by_re = re.compile(
    'X-Powered-By: (?P<x_powered_by>.+?)\r?\n',
    flags=re.IGNORECASE)


def write_to_csv(row):
    """
    Writes a csv row to a csv file.

    Args:
        row: (str): write your description
    """
    with open(OUTFILE, 'a+') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(row)
    csvfile.close()


def get_x_powered_by(html):
    """
    Get x - x x - x - x - y - x - x - x - y - x - x - x - x - y -

    Args:
        html: (str): write your description
    """
    match_obj = x_powered_by_re.search(html)
    if match_obj is not None:
        match_obj = match_obj.group('x_powered_by').strip()
    return match_obj


def get_content_type(html):
    """
    Return the content type of the content type.

    Args:
        html: (todo): write your description
    """
    match_obj = content_type_re.search(html)
    if match_obj is not None:
        match_obj = match_obj.group('content_type').strip()
    return match_obj


def get_content_encoding(html):
    """
    Get content encoding.

    Args:
        html: (str): write your description
    """
    match_obj = content_encoding_re.search(html)
    if match_obj is not None:
        match_obj = match_obj.group('content_encoding').strip()
    return match_obj


def get_server(html):
    """
    Returns the server.

    Args:
        html: (str): write your description
    """
    match_obj = server_re.search(html)
    if match_obj is not None:
        match_obj = match_obj.group('server').strip()
    return match_obj


def get_title(html):
    """
    Get title.

    Args:
        html: (todo): write your description
    """
    match_obj = title_re.search(html)
    if match_obj is not None:
        match_obj = match_obj.group('title').strip()
    return match_obj


def get_last_modified(html):
    """
    Get the last modified modification of an object.

    Args:
        html: (str): write your description
    """
    match_obj = last_modified_re.search(html)
    if match_obj is not None:
        match_obj = match_obj.group('last_modified').strip()
    return match_obj


def to_ascii(data):
    """
    Convert data to utf8.

    Args:
        data: (todo): write your description
    """
    if isinstance(data, str):
        return data.encode("ascii", errors="ignore")
    elif isinstance(data, bytes):
        return data.decode("ascii", errors="ignore")


def to_utf(data):
    """
    Convert a string to utf.

    Args:
        data: (todo): write your description
    """
    if isinstance(data, str):
        return data.encode("utf8", errors="ignore")
    elif isinstance(data, bytes):
        return data.decode("utf8", errors="ignore")


server_vers = []
host_server = []
port_no = ""

ignore_hosts = [
    "Apache",
    "nginx",
    "Microsoft",
    "lighttpd",
    "xxxxxxxx-xxxxx",
    "xxxx"]


def parse_json_zips():
    """
    Parse the zips.

    Args:
    """
    for INFILE in glob.glob("*.json.gz"):
        #######################################################################
        # this is needed to identify the different data sets, by port number.
        #######################################################################
        port_no = INFILE.replace('.json.gz', '')
        port_no = str(port_no.split('_')[-1])
        #######################################################################
        # this is needed to identify the different data sets, by port number.
        #######################################################################
        print("[+] debug, port:..." + str(port_no))
        with gzip.open(INFILE) as f:
            print('[+] Parsing JSON: {}'.format(INFILE))
            for line in f:
                tmp_lst = []
                html_data = json.loads(line)
                decoded_data = to_ascii(base64.b64decode(html_data["data"]))
                server_header_name = get_server(decoded_data)
                if server_header_name is not None:
                    if not any(
                            x in server_header_name for x in ignore_hosts):  # remove common servers
                        tmp_lst.append(
                            str(html_data["host"]) + ":" + str(port_no))
                        # tmp_lst.append(get_title(decoded_data)) #not in use,
                        # Apr 2020
                        tmp_lst.append(server_header_name)
                        server_vers.append(server_header_name)
                        # tmp_lst.append(get_content_type(decoded_data)) #not in use, Apr 2020
                        # tmp_lst.append(get_content_encoding(decoded_data)) #not in use, Apr 2020
                        # tmp_lst.append(get_x_powered_by(decoded_data)) #not in use, Apr 2020
                        # tmp_lst.append(get_last_modified(decoded_data)) #not
                        # in use, Apr 2020
                        host_server.append(tmp_lst)
                        # write_to_csv(tmp_lst) #not in use, Apr 2020


def parse_json_headers():
    """
    Parses the headers.

    Args:
    """
    headers = {}
    for INFILE in glob.glob("*.json.gz"):
        # this is needed to identify the different data sets, by port number.
        port_no = INFILE.replace('.json.gz', '')
        # this is needed to identify the different data sets, by port number.
        port_no = str(port_no.split('_')[-1])
        # this is needed to identify the different data sets, by port number.
        print("[+]debug, port:..." + str(port_no))
        with gzip.open(INFILE) as f:
            print('[+] Parsing JSON: {}'.format(INFILE))
            for line in f:
                html_data = json.loads(line)
                decoded_data = to_ascii(base64.b64decode(html_data["data"]))

                match_obj = header_section_re.search(decoded_data)
                if match_obj is None:
                    continue

                for header in match_obj.group('headers').split('\n'):
                    header_match = header_re.search(header)
                    if header_match is None:
                        continue
                    if header_match.group('name').strip() not in headers:
                        headers[header_match.group('name').strip()] = 0
                    headers[header_match.group('name').strip()] += 1
    return headers


parse_json_zips()
# debug,debug,debug,debug ----> counting the occurances of each type to fine tune. Helps create ignore_hosts above
# print(pd.Series(server_vers).value_counts().to_string())
#series_txt_file = open('data.txt', 'w')
# series_txt_file.write(pd.Series(server_vers).value_counts().to_string())
# series_txt_file.close()

df = pd.DataFrame(host_server, columns=['Host', 'Server'])
df.sort_values(by=['Server'], ascending=True)
series_txt_file = open('df_servers.txt', 'w')
series_txt_file.write(df.to_string())
series_txt_file.close()
###############################################
###############################################
###############################################
OSINT_search_list = ["squid", "proxy"]


def check_proxy(proxies_dicts):
    """
    Check if a http proxy.

    Args:
        proxies_dicts: (dict): write your description
    """
    try:
        r = requests.get(
            random.choice(check_ip),
            headers={
                'User-Agent': ua.random},
            verify=False, timeout=0.5,proxies=proxies_dicts)
        # print(r.status_code)
        if int(r.status_code) == 200:
            print("[+]debug, potential open proxy found:" + str(proxies_dicts))
            print(r.text)
        r.raise_for_status()

    except requests.exceptions.HTTPError as errh:
        #print ("Http Error:",errh)
        return None
    except requests.exceptions.ConnectionError as errc:
        #print ("Error Connecting:",errc)
        return None
    except requests.exceptions.Timeout as errt:
        #print ("Timeout Error:",errt)
        return None
    except requests.exceptions.RequestException as err:
        #print ("OOps: Something Else",err)
        return None
    except BaseException as e:
        print(e)
        return None


#################################################
for each in OSINT_search_list:
    squid_list = df[df['Server'].str.contains(each)]
    # print(squid_list['Host'].tolist())

proxies_dicts = []

for each_proxy in squid_list['Host'].tolist():
    #http_proxy = "http://" + str(each_proxy)
    https_proxy = "https://" + str(each_proxy)
    proxyDict = {
        "http": http_proxy,
        "https": https_proxy,
        "ftp": ftp_proxy}
    proxies_dicts.append(proxyDict)

    with ThreadPoolExecutor(max_workers=len(each_proxy)) as pool:
        pool.map(check_proxy, proxies_dicts)
