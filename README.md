# rapid7_OSINT

So as most of us we have found ourselves with alot of time on our hands and only bound by imagination. Who ever said "If a hacker is ever bored, He will be quickly become not bored" Not that I condone hacking of any kind! No systems were breached here, **All of this is done by using already publicly available information.** But I suspect because of the "gold rush" to setup systems for working from homes, We are racing to the bottoms in terms of bad administration and bad understanding of how systems are actually put together, All of a sudden in many organisations across the world Bob from Accounts has become the unwitting "Sysadmin".

I thought I would have a look around the Rapid 7 Open Data Sets (which are fantastic by the way)....*And also release some quick tools.* 

So let's start with the standard stuff, Remove the monopoly"Web Servers"...Apache, nginx, Microsoft, lighttpd, xxxxxxxx-xxxxx, xxxx. These have their own tools and associated problems and this is not in scope here. We are looking here for the interesting, quirky, slightly obscure. Mainly IoT Devices, Some uncommon stuff. Cameras, Printers, Service Control Mechanisms etc.

**default searches** 

* "HP" - Printers, iLO devices!  Nothing personal but this is low hanging fruit. Alot of these include the serial number in clear text. If you are a "Social Engineer" of sorts I am sure this is useful to some. 
* "phone" - Video conferencing is a big thing now right?? Wonder who these belong to and if you can just join int? 
* "cisco" - Unwitting Sysadmin who have exposted their core network to the world. 
* "DVR" - Free TV right from the comfort of your own living room... or someone elses. 
* "Index of" - Free stuff
* "Schneider" - Electrical control system
* "Industrial"  - Electrical control system

Special shout out goes to...."search" - Elastic Search Databases. I don't need to tell you..

* 2018-11-15 AWS Elasticsearch database belonging to VoxOx exposed tens of millions of text messages, including password reset links, two-factor codes, shipping notifications and more.
* 2018-11-27 Elasticsearch database belonging to Urban Massage exposed more than 309,000 user records, including names, email addresses and phone numbers.
* 2019-01-12 Elasticsearch server belonging to do-it-yourself chain, B&Q exposed personal details of individuals caught or suspected of stealing goods from stores.
* 2019-01-21 Elasticsearch database belonging to Youth-run agency AIESEC exposed over 4 million intern applications including the applicant’s name, gender, date of birth, and the reasons why the person was applying for the internship.
* 2019-01-23 Elasticsearch database belonging to Ascension Data and Analytics exposed 24 million financial and banking documents, representing tens of thousands of loans and mortgages from some of the biggest banks in the U.S.
* 2019-09-13 Elasticsearch database belonging to Dealer Leads exposed 198 million car buying records which contained the personal information of customers.
* 2019-10-26 Elasticsearch database belonging to Adobe exposed 7.5 million customer records which contained email addresses, Adobe member IDs (usernames), country of origin, and what Adobe products they were using.
* 2019-11-19 Elasticsearch database belonging to Conrad Electronic exposed 14 million customer records which contained postal addresses, in parts fax- and telephone numbers as well as IBANs on a fifth of the exposed data-records.

And many many more ones that have gone unreported. 

Here I looked at Port **4443** and port **5001** and this is the list of services minus the ones removed as discussed.

https://raw.githubusercontent.com/tg12/rapid7_OSINT/master/data.txt

This is a count of how often each server type if you will occurs. 

Here is a list URL/Size in MB, It's organised by port number. It's a trade off by file size and what ports would be useful and most common. I don't have enough disk space on any of my fast VPS's to get the large one but I'd like to some day. 


*     https://opendata.rapid7.com/sonar.https/2020-03-22-1584882568-https_get_16993.json.gz		2.04216
*     https://opendata.rapid7.com/sonar.https/2020-03-21-1584798976-https_get_7550.json.gz		2.06119
*     https://opendata.rapid7.com/sonar.https/2020-03-22-1584891983-https_get_50880.json.gz		2.33534
*     https://opendata.rapid7.com/sonar.https/2020-03-21-1584760512-https_get_7548.json.gz		2.55314
*     https://opendata.rapid7.com/sonar.https/2020-03-21-1584833677-https_get_8984.json.gz		4.29511
*     https://opendata.rapid7.com/sonar.https/2020-03-04-1583300084-https_get_6984.json.gz		4.65733
*     https://opendata.rapid7.com/sonar.https/2020-03-23-1584943465-https_get_49592.json.gz		7.06081
*     https://opendata.rapid7.com/sonar.https/2020-03-23-1584964760-https_get_55443.json.gz		12.2823
*     https://opendata.rapid7.com/sonar.https/2020-03-23-1584978247-https_get_9043.json.gz		12.2978
*     https://opendata.rapid7.com/sonar.https/2020-03-22-1584880758-https_get_8009.json.gz		16.5622
*     https://opendata.rapid7.com/sonar.https/2020-03-21-1584813064-https_get_7002.json.gz		16.7793
*     https://opendata.rapid7.com/sonar.https/2020-03-23-1584964943-https_get_12443.json.gz		25.7956
*     https://opendata.rapid7.com/sonar.https/2020-03-20-1584735346-https_get_3001.json.gz		32.123
*     https://opendata.rapid7.com/sonar.https/2020-03-23-1584949299-https_get_30443.json.gz		32.1281
*     https://opendata.rapid7.com/sonar.https/2020-03-21-1584794811-https_get_8002.json.gz		32.5078
*     https://opendata.rapid7.com/sonar.https/2020-03-23-1584972264-https_get_44443.json.gz		33.3802
*     https://opendata.rapid7.com/sonar.https/2020-03-23-1584970464-https_get_40443.json.gz		37.4274
*     https://opendata.rapid7.com/sonar.https/2020-03-23-1584975815-https_get_60443.json.gz		42.9166
*     https://opendata.rapid7.com/sonar.https/2020-03-23-1584951256-https_get_50443.json.gz		46.3311
*     https://opendata.rapid7.com/sonar.https/2020-03-20-1584691134-https_get_2443.json.gz		60.4992
*     https://opendata.rapid7.com/sonar.https/2020-03-21-1584766137-https_get_4434.json.gz		64.0676
*     https://opendata.rapid7.com/sonar.https/2020-03-23-1584944299-https_get_11443.json.gz		64.1328
*     https://opendata.rapid7.com/sonar.https/2020-03-21-1584774150-https_get_7443.json.gz		101.514
*     https://opendata.rapid7.com/sonar.https/2020-03-22-1584847578-https_get_8010.json.gz		122.659
*     https://opendata.rapid7.com/sonar.https/2020-03-21-1584772142-https_get_5443.json.gz		131.028
*     https://opendata.rapid7.com/sonar.https/2020-03-23-1584955483-https_get_8181.json.gz		167.702
*     https://opendata.rapid7.com/sonar.https/2020-03-20-1584741308-https_get_4343.json.gz		240.773
*     https://opendata.rapid7.com/sonar.https/2020-03-23-1584957330-https_get_10443.json.gz		247.274
*     https://opendata.rapid7.com/sonar.https/2020-03-22-1584904101-https_get_8090.json.gz		249.368
*     https://opendata.rapid7.com/sonar.https/2020-03-23-1584921753-https_get_9443.json.gz		280.97
*     https://opendata.rapid7.com/sonar.https/2020-03-20-1584677242-https_get_1443.json.gz		304.378
*     **https://opendata.rapid7.com/sonar.https/2020-03-23-1584935946-https_get_5001.json.gz		661.486**
*     **https://opendata.rapid7.com/sonar.https/2020-03-21-1584826266-https_get_4443.json.gz		804.583**
*     https://opendata.rapid7.com/sonar.https/2020-03-01-1583021118-https_get_top1m.json.gz		1704.61
*     https://opendata.rapid7.com/sonar.https/2020-03-21-1584761791-https_get_4433.json.gz		1798.67
*     https://opendata.rapid7.com/sonar.https/2020-03-22-1584917234-https_get_8443.json.gz		2677.11
*     https://opendata.rapid7.com/sonar.https/2020-03-20-1584718963-https_get_2087.json.gz		19736.1
*     https://opendata.rapid7.com/sonar.https/2020-03-20-1584708738-https_get_2083.json.gz		22652.3
*     https://opendata.rapid7.com/sonar.https/2020-03-23-1584982725-https_get_443.json.gz		59172.4


I have noticed odditys such as things like "Wing FTP Server"... there are a few occurrences of this. Do they publish the Liscened user in the header? ....again one for you Social Engineers out there. I am sure there is bound to be alot more in the bigger files. One to watch perhaps?. 

    * Wing FTP Server(tonyweb)
    * Wing FTP Server(J Wyndham Prince Pty Ltd)
    * Wing FTP Server(Atik Srl)
    * Wing FTP Server(DIGITAL UNLIMITED GROUP LTD)
    * Wing FTP Server(Mario Kaserer)
    * Wing FTP Server(Imanaka Kudo & Fujimoto)
    * Wing FTP Server(WAB Sicherheitssysteme GmbH)
    * Wing FTP Server(Spatial Engineerin)
    * Wing FTP Server(CDS software) 
    * Wing FTP Server(Semmes Bowen & Semmes)
    * Wing FTP Server(Daktronics)   
    * Wing FTP Server(MicroMain)    
    * Wing FTP Server(SDA Informatika Zrt)
    * Wing FTP Server(afcon.it)
    * Wing FTP Server(Atlantis Media Group)
    * Wing FTP Server(Innova Bilisim Cozumleri)

Can you think of anything else interesting to look for? Take a look. Fork and change the search parameters. 

Thanks for reading.

Massive Thanks to…

- Rapid 7…

https://opendata.rapid7.com

**I am not affiliated, associated, authorized, endorsed by, or in any way officially connected with rapid7.com, or any of its subsidiaries or its affiliates.**

**THE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR ANYONE DISTRIBUTING THE SOFTWARE BE LIABLE FOR ANY DAMAGES OR OTHER LIABILITY, WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THIS OR THE USE OR OTHER DEALINGS.** 

If you feel you liked this and it was useful, Please help me out rent a bigger VPS to get the bigger datasets. 

[Paypal Donate](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=EV8XUGXX76UXQ&source=url)

###### Bitcoin Cash (BCH)  - 	  qpz32c4lg7x7lnk9jg6qg7s4uavdce89myax5v5nuk
###### Ether (ETH) - 				    0x843d3DEC2A4705BD4f45F674F641cE2D0022c9FB
###### Litecoin (LTC) - 			  Lfk5y4F7KZa9oRxpazETwjQnHszEPvqPvu
###### Bitcoin (BTC) - 			    14Dm7L3ABPtumPDcj3REAvs4L6w9YFRnHK
