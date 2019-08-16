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

# Note, The free data changes once a month. Use this to download the
# latest files.

from __future__ import print_function
import os
import sys
import bs4
import requests
from operator import itemgetter
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

base_url = "https://opendata.rapid7.com"
url = 'https://opendata.rapid7.com/sonar.http/'
ext = '.json.gz'
url_and_size = []

# number of bytes in a megabyte
MBFACTOR = float(1 << 20)


def extract(content):
    links = []
    soup = bs4.BeautifulSoup(content)
    for tag in soup.find_all():
        if tag.name == 'a' and 'href' in tag.attrs:
            links.append(tag.attrs['href'])
    return links


content = requests.get(url, verify=False).text
links = extract(content)

for each_link in links:
    if ext in each_link:
        tmp_lst = []
        tmp_lst.append(base_url + each_link)
        response = requests.head(
            base_url + each_link,
            allow_redirects=True,
            verify=False)
        # print("\n".join([('{:<40}: {}'.format(k, v)) for k, v in response.headers.items()]))
        size = response.headers.get('content-length', 0)
        # print('{:<40}: {:.2f} MB'.format('FILE SIZE', int(size) / MBFACTOR))
        tmp_lst.append(float(int(size) / MBFACTOR))
        url_and_size.append(tmp_lst)

for each in sorted(url_and_size, key=itemgetter(1)):
     print(each[0])  # url
     print(each[1])  # size in MB
     file_name = each[0].split('/')[-1]
     if os.path.exists(file_name) == False:
         try:
             with open(file_name, 'wb') as f:
                 f.write(requests.get(each[0]).content)
         except:
             print('Unable to download file: {}'.format((each[0])))
