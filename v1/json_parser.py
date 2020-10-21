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

# Dont forget to tip your server!
# Bitcoin Cash (BCH)   qpz32c4lg7x7lnk9jg6qg7s4uavdce89myax5v5nuk
# Ether (ETH) -        0x843d3DEC2A4705BD4f45F674F641cE2D0022c9FB
# Litecoin (LTC) -     Lfk5y4F7KZa9oRxpazETwjQnHszEPvqPvu
# Bitcoin (BTC) -      34L8qWiQyKr8k4TnHDacfjbaSqQASbBtTd

# I am not affiliated, associated, authorized, endorsed by, or in any way officially connected with rapid7.com, or any of its subsidiaries or its affiliates.
# https://opendata.rapid7.com/sonar.http/
# https://github.com/rapid7/sonar/wiki/HTTP

import json
import gzip
import base64
import time
from collections import Counter
import csv
import glob
import re
import os

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

header_section_re = re.compile('HTTP/(?P<version>\d+\.?\d*) (?P<status>\d+ .+?)((\r\n)|(\n))(?P<headers>.+?)((\r\n\r\n)|(\n\n))', flags=re.DOTALL)
header_re = re.compile('(?P<name>.+?): (?P<value>.+)(\r?)')
title_re = re.compile('(\<title\>)(?P<title>.+?)(\</title\>)', flags=re.IGNORECASE)
server_re = re.compile('Server: (?P<server>.+?)\r?\n', flags=re.IGNORECASE)
content_type_re = re.compile('Content-Type: (?P<content_type>.+?)\r?\n', flags=re.IGNORECASE)
content_encoding_re = re.compile('Content-Encoding: (?P<content_encoding>.+?)\r?\n', flags=re.IGNORECASE)
last_modified_re = re.compile('Last-Modified: (?P<last_modified>.+?)\r?\n', flags=re.IGNORECASE)
x_powered_by_re = re.compile('X-Powered-By: (?P<x_powered_by>.+?)\r?\n', flags=re.IGNORECASE)


def write_to_csv(row):
    with open(OUTFILE, 'a+') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(row)
    csvfile.close()

def get_x_powered_by(html):
    match_obj = x_powered_by_re.search(html)
    if match_obj != None:
        match_obj = match_obj.group('x_powered_by').strip()
    return match_obj

def get_content_type(html):
    match_obj = content_type_re.search(html)
    if match_obj != None:
        match_obj = match_obj.group('content_type').strip()
    return match_obj

def get_content_encoding(html):
    match_obj = content_encoding_re.search(html)
    if match_obj != None:
        match_obj = match_obj.group('content_encoding').strip()
    return match_obj

def get_server(html):
    match_obj = server_re.search(html)
    if match_obj != None:
        match_obj = match_obj.group('server').strip()
    return match_obj

def get_title(html):
    match_obj = title_re.search(html)
    if match_obj != None:
        match_obj = match_obj.group('title').strip()
    return match_obj

def get_last_modified(html):
    match_obj = last_modified_re.search(html)
    if match_obj != None:
        match_obj = match_obj.group('last_modified').strip()
    return match_obj

def to_ascii(data):
    if isinstance(data, str):
        return data.encode("ascii", errors="ignore")
    elif isinstance(data, bytes):
        return data.decode("ascii", errors="ignore")

def to_utf(data):
    if isinstance(data, str):
        return data.encode("utf8", errors="ignore")
    elif isinstance(data, bytes):
        return data.decode("utf8", errors="ignore")

def parse_json_zips():
    for INFILE in glob.glob("*.json.gz"):
        port_no = INFILE.replace('.json.gz', '') # this is needed to identify the different data sets, by port number.
        port_no = str(port_no.split('_')[-1]) # this is needed to identify the different data sets, by port number.
        print("[+]debug, port:..." + str(port_no)) # this is needed to identify the different data sets, by port number.
        with gzip.open(INFILE) as f:
            print('[+] Parsing JSON: {}'.format(INFILE))
            for line in f:
                tmp_lst = []
                html_data = json.loads(line)
                decoded_data = to_ascii(base64.b64decode(html_data["data"]))
                tmp_lst.append(str(html_data["host"]) + ":" + str(port_no))
                tmp_lst.append(get_title(decoded_data))
                tmp_lst.append(get_server(decoded_data))
                tmp_lst.append(get_content_type(decoded_data))
                tmp_lst.append(get_content_encoding(decoded_data))
                tmp_lst.append(get_x_powered_by(decoded_data))
                tmp_lst.append(get_last_modified(decoded_data))
                write_to_csv(tmp_lst)

def parse_json_headers():
    headers = {}
    for INFILE in glob.glob("*.json.gz"):
        port_no = INFILE.replace('.json.gz', '') # this is needed to identify the different data sets, by port number. 
        port_no = str(port_no.split('_')[-1])   # this is needed to identify the different data sets, by port number.
        print("[+]debug, port:..." + str(port_no)) # this is needed to identify the different data sets, by port number.
        with gzip.open(INFILE) as f:
            print('[+] Parsing JSON: {}'.format(INFILE))
            for line in f:
                html_data = json.loads(line)
                decoded_data = to_ascii(base64.b64decode(html_data["data"]))
                
                match_obj = header_section_re.search(decoded_data)
                if match_obj == None:
                    continue
                
                for header in match_obj.group('headers').split('\n'):
                    header_match = header_re.search(header)
                    if header_match == None:
                        continue
                    if header_match.group('name').strip() not in headers:
                        headers[header_match.group('name').strip()] = 0
                    headers[header_match.group('name').strip()] += 1
    return headers

parse_json_zips()

#headers = parse_json_headers()
#sorted_x = sorted(headers.items(), key=operator.itemgetter(1), reverse=True)
#with open('http_headers_by_commonality.txt', 'w') as f:
#    for pair in sorted_x:
#        print('{}: {}'.format(pair[0], pair[1]))
#        f.write('{}: {}\n'.format(pair[0], pair[1]))
