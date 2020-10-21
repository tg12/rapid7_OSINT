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
from tabulate import tabulate
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from fake_useragent import UserAgent
ua = UserAgent()

base_url = "https://opendata.rapid7.com"
url = 'https://opendata.rapid7.com/sonar.http/'
ext = '.json.gz'
url_and_size = []

# number of bytes in a megabyte
MBFACTOR = float(1 << 20)

#thanks to:https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/
def Sort(sub_li): 
    l = len(sub_li) 
    for i in range(0, l): 
        for j in range(0, l-i-1): 
            if (sub_li[j][1] > sub_li[j + 1][1]): 
                tempo = sub_li[j] 
                sub_li[j]= sub_li[j + 1] 
                sub_li[j + 1]= tempo 
    return sub_li 

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
            verify=False, headers={
                'User-Agent': ua.random})
        # print("\n".join([('{:<40}: {}'.format(k, v)) for k, v in response.headers.items()]))
        size = response.headers.get('content-length', 0)
        # print('{:<40}: {:.2f} MB'.format('FILE SIZE', int(size) / MBFACTOR))
        tmp_lst.append(float(int(size) / MBFACTOR))
        url_and_size.append(tmp_lst)

sorted_li = Sort(url_and_size)
print(tabulate(sorted_li, headers=['URL', 'Size']))

for each in sorted(url_and_size, key=itemgetter(1)):
      print(each[0])  # url
      with open("http_urls.txt", 'a') as http_urls:
        http_urls.write(str(each[0]) + "\n")
#      print(each[1])  # size in MB

# for each in sorted(url_and_size, key=itemgetter(1)):
     # print(each[0])  # url
     # print(each[1])  # size in MB
     # file_name = each[0].split('/')[-1]
     # if os.path.exists(file_name) == False:
         # try:
             # with open(file_name, 'wb') as f:
                 # f.write(requests.get(each[0]).content)
         # except:
             # print('Unable to download file: {}'.format((each[0])))