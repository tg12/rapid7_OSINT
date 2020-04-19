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

# I am not affiliated, associated, authorized, endorsed by, or in any way
# officially connected with rapid7.com, or any of its subsidiaries or its
# affiliates.

# https://opendata.rapid7.com/sonar.http/
# https://github.com/rapid7/sonar/wiki/HTTP
import json
import gzip
import base64
import time
import datetime
from collections import Counter
from fake_useragent import UserAgent
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests
import re
import bs4
import csv
import glob
import os
import threading
import socket
import whois
from termcolor import colored
##############################
# comments
##############################
# This will produce two CSV's
# The hostname and the title page that was found on said port
# The enumeration of "Index of /" It might show up some juicy stuff? Who
# knows. (Absolutely will)

INDEXFILENAME = "index_of_" + time.strftime("%Y%m%d-%H%M%S") + ".csv"
FULLTITLEFILE = "full_title_" + time.strftime("%Y%m%d-%H%M%S") + ".csv"

title_data = []
uniq_titles = []
max_pages = int(30)
ua = UserAgent()
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# ua = UserAgent(verify_ssl=False, use_cache_server=False)
# ua.update()


def diff_dates(date1, date2):
    return abs((date2 - date1).days)


def whois_domain(domain_name):

    RES = {}
    try:
        w_res = whois.whois(domain_name)
        name = w_res.name
        creation_date = w_res.creation_date
        emails = w_res.emails
        registrar = w_res.registrar
        updated_date = w_res.updated_date
        expiration_date = w_res.expiration_date

        if isinstance(
                creation_date,
                datetime.datetime) or isinstance(
                expiration_date,
                datetime.datetime) or isinstance(
                updated_date,
                datetime.datetime):
            current_date = datetime.datetime.now()
            res = diff_dates(current_date, creation_date)
            RES.update({"creation_date": creation_date,
                        "creation_date_diff": res,
                        "emails": emails,
                        "name": name,
                        "registrar": registrar,
                        "updated_date": updated_date,
                        "expiration_date": expiration_date})

        elif isinstance(creation_date, list) or isinstance(expiration_date, list) or isinstance(updated_date, list):
            creation_date = w_res.creation_date[0]
            updated_date = w_res.updated_date[0]
            expiration_date = w_res.expiration_date[0]
            current_date = datetime.datetime.now()
            res = diff_dates(current_date, creation_date)

            RES.update({"creation_date": creation_date,
                        "creation_date_diff": res,
                        "emails": emails,
                        "name": name,
                        "registrar": registrar,
                        "updated_date": updated_date,
                        "expiration_date": expiration_date})

        time.sleep(2)
    except TypeError:
        pass
    except whois.parser.PywhoisError:
        print(colored("No match for domain: {}.".format(domain_name), 'red'))
    except AttributeError:
        pass
    except Exception as e:
        print(e)
    return RES


web_server_ports = [80,
                    49153,
                    9060,
                    16992,
                    6066,
                    60000,
                    8899,
                    50880,
                    9001,
                    8888,
                    18080,
                    8081,
                    4040,
                    5000,
                    49152,
                    9990,
                    9000,
                    8820,
                    8080,
                    65535,
                    8545,
                    8500,
                    8001,
                    7549,
                    5431,
                    7011,
                    7001,
                    4000,
                    5555,
                    7548,
                    9002,
                    8088,
                    8983,
                    8060,
                    8008,
                    7000,
                    2004,
                    4567,
                    8761,
                    7547,
                    4001,
                    7100,
                    3000,
                    7010,
                    3689,
                    1400,
                    7077,
                    6060,
                    666,
                    3128,
                    2082,
                    2086,
                    1024,
                    5984,
                    9200]


def spider(base_url):
    auxiliaryList = []
    page_id = 1
    print("[+]debug, checking..." + str(base_url))
    while page_id <= max_pages:
        try:
            headers = {'User-Agent': ua.random}
            page = requests.get(
                base_url, verify=False, headers=headers, timeout=4)
            soup = bs4.BeautifulSoup(page.text, features="html.parser")
            for link in soup.find_all('a'):
                if link.get('href') not in auxiliaryList:
                    auxiliaryList.append(base_url + link.get('href'))
            page_id = page_id + 1
        except Exception as exc:
            # print(exc) #debug, if one fails dont punish the rest!!
            continue
            page_id = page_id + 1

    for each_link in auxiliaryList:
        try:
            tmp_lst = []
            r = requests.get(
                each_link,
                verify=False,
                headers=headers,
                timeout=4)
            html = bs4.BeautifulSoup(r.text, features="html.parser")
            if "Index of " in str(html.title.text):
                print("[+]debug, found! ... " + str(html.title.text))
                print("[+]debug, found! ... " + str(each_link))
                tmp_lst.append(str(html.title.text))
                tmp_lst.append(str(each_link))
                # write out to csv here, only the "Index of stuff"
                with open(INDEXFILENAME, 'a+') as index_of_list:
                    wr = csv.writer(index_of_list, dialect='excel')
                    wr.writerow(tmp_lst)
                index_of_list.close()
                print("################")
        except Exception as exc:
            # print(exc) #debug, just timeouts for requests. If one fails dont
            # punish the rest!!
            continue


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

for rapid7_file in glob.glob("*.json.gz"):
    print("[+]debug, file..." + str(rapid7_file))

    with gzip.open(rapid7_file) as f:
        for line in f:
            tmp_lst = []
            html_data = json.loads(line)

            title = get_title(to_ascii(base64.b64decode(html_data["data"])))
            if title is not None:
                if title is not "":
                    if any(x in title for x in bypass_err):
                        # print("[-]debug, error found in string")
                        pass
                    else:  # clear
                        try:
                            try:
                                host_id = socket.gethostbyaddr(
                                    str(html_data["host"]))[0]
                                tmp_lst.append(host_id)
                            except Exception as exc:
                                host_id = html_data["host"]
                                tmp_lst.append(host_id)
                            tmp_lst.append(html_data["path"])
                            tmp_lst.append(title)
                            try:
                                whois_data = whois_domain(host_id)
                                if whois_data:
                                    for k, v in whois_data.items():
                                        # if 'creation_date' in k:
                                            # cd = whois_data.get('creation_date')
                                        # if 'updated_date' in k:
                                            # ud = whois_data.get('updated_date')
                                        # if 'expiration_date' in k:
                                            # ed = whois_data.get('expiration_date')
                                        # if 'creation_date_diff' in k:
                                            # cdd = whois_data.get('creation_date_diff')
                                        if 'name' in k:
                                            name = whois_data.get('name')
                                            tmp_lst.append(name)
                                        # if 'emails' in k:
                                            # email = whois_data.get('emails')
                                        # if 'registrar' in k:
                                            # reg = whois_data.get('registrar')
                            except Exception as exc:
                                print(exc)
                                pass
                            uniq_titles.append(title)
                            title_data.append(tmp_lst)
                            # write out to csv file here (all data)
                            with open(FULLTITLEFILE, 'a+') as full_title_scan:
                                wr = csv.writer(
                                    full_title_scan, dialect='excel')
                                wr.writerow(tmp_lst)
                            full_title_scan.close()
                            print("adding,... " + str(tmp_lst))
                            # OSINT Stuff here, Index of etc.
                            thread_list = []
                            if "Index of /" in str(title):
                                for web_port in web_server_ports:  # check other web server ports just incase
                                    thread = threading.Thread(target=spider, args=(
                                        "http://" + str(host_id) + ":" + str(web_port),))
                                    thread_list.append(thread)
                                    thread.start()
                        except Exception as exc:
                            # print(exc) #debug, probs too many files open, fix
                            # later or continue on
                            pass
