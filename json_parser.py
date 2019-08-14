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


def write_to_csv(row):
    with open(OUTFILE, 'a+') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(row)
    csvfile.close()


def get_title(html):
    html_lowered = html.lower()
    begin = html_lowered.find('<title>')
    end = html_lowered.find('</title>')
    if begin == -1 or end == -1:
        return None
    else:
        # Find in the original html
        return html[begin + len('<title>'):end].strip()


def to_ascii(data):
    if isinstance(data, str):
        return data.encode("ascii", errors="ignore")
    elif isinstance(data, bytes):
        return data.decode("ascii", errors="ignore")


for INFILE in glob.glob("*.json.gz"):
    with gzip.open(INFILE) as f:
        port_no = INFILE.replace('.json.gz', '')
        port_no = str(port_no.split('_')[-1])
        print("[+]debug, port:..." + str(port_no))
        for line in f:
            tmp_lst = []
            html_data = json.loads(line)

            title = get_title(to_ascii(base64.b64decode(html_data["data"])))
            if title is not None:
                if title is not "":
                    if any(x in title for x in bypass_err):
                        # print("[-]debug, error found in string")
                        pass
                    else:
                        tmp_lst.append(
                            str(html_data["host"]) + ":" + str(port_no))
                        tmp_lst.append(title)
                        print("adding,... " + str(tmp_lst))
                        write_to_csv(tmp_lst)
