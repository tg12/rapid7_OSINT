# rapid7_OSINT

**default searches** 

* "HP" - Printers, iLO devices!  Nothing personal against HP but it's low hanging fruit Alot of these include the serial number in clear text. If you are a "Social Engineer" of sorts I am sure this is useful to some. 
* "phone" - Lot's of open phones that should not be exposed.
* "cisco" - Unwitting Sysadmin who have exposted their core network to the world. 
* "DVR" - Free TV right from the comfort of your own living room... or someone elses. 
* "Index of" - Free stuff
* "Schneider" - Electrical control system
* "Industrial"  - Electrical control system

Remove the monopoly "Web Servers"...Apache, nginx, Microsoft, lighttpd, xxxxxxxx-xxxxx, xxxx. 
These have their own tools and associated problems and this is not in scope here. We are looking here for the interesting, quirky, slightly obscure. Mainly IoT Devices, Some uncommon stuff. Cameras, Printers, Service Control Mechanisms etc.

Here I looked at **most" ports excluding the big files and this is the list of services minus the ones removed as discussed.

https://raw.githubusercontent.com/tg12/rapid7_OSINT/master/list_of_servers.txt

This is a count of how often each server type if you will occurs. 

in the "scans" folder I have included two. One very interesting which I had to Google. Scary stuff...

* https://sec-consult.com/en/blog/2018/05/tr-069-iot-before-it-was-cool/ Basically remote management for CPE devices (home broadband)

* The other Hikvision, The popular home security cameras. 

Thanks for reading.

Massive Thanks to…

- Rapid 7

https://opendata.rapid7.com

**I am not affiliated, associated, authorized, endorsed by, or in any way officially connected with rapid7.com, or any of its subsidiaries or its affiliates.**

**THE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR ANYONE DISTRIBUTING THE SOFTWARE BE LIABLE FOR ANY DAMAGES OR OTHER LIABILITY, WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THIS OR THE USE OR OTHER DEALINGS.** 

If you feel you liked this and it was useful, Please help me out rent a bigger VPS to get the bigger datasets. 

[Paypal Donate](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=EV8XUGXX76UXQ&source=url)

###### Bitcoin Cash (BCH)  - 	  qpz32c4lg7x7lnk9jg6qg7s4uavdce89myax5v5nuk
###### Ether (ETH) - 				    0x843d3DEC2A4705BD4f45F674F641cE2D0022c9FB
###### Litecoin (LTC) - 			  Lfk5y4F7KZa9oRxpazETwjQnHszEPvqPvu
###### Bitcoin (BTC) - 			    14Dm7L3ABPtumPDcj3REAvs4L6w9YFRnHK
