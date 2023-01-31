# Web sniffer
***


## Table of Contents
1. [Description](#description)
2. [Warning](#warning)
3. [Compatibilities](#compatibilities)
4. [Installation](#installation)
5. [How to use](#usage)
6. [Features](#features)
7. [Contributing](#contributing)

### Description:
***
This project try to sniff local network to get sensible informations 


### Warning:
***
You need to use this tool only on network that you owned.
\
You need to consult your country's laws before using it. 

### Compatibilities
***
Python 3.6+


### Installation
***
Please read [requirements.txt](https://github.com/juste-sebastien/sniffer/blob/master/requirements.txt) to get all libs using with this project and use the package manager [pip](https://pip.pypa.io/en/stable/) to install them.

```bash
git clone https://github.com/juste-sebastien/sniffer
cd path/to/the/file
```

### How to use
***
```commandline
python3 main.py -iface [interface]
```
and wait for result like this:

```commandline
[*] None
###[ Ethernet ]### 
  dst       = 
  src       = 
  type      = IPv4
###[ IP ]### 
     version   = 4
     ihl       =
     tos       =
     len       =
     id        =
     flags     =
     frag      = 0
     ttl       =
     proto     = 
     chksum    =
     src       = 
     dst       = 
     \options   \
###[ TCP ]### 
        sport     = 
        dport     = http
        seq       = 
        ack       = 
        dataofs   = 
        reserved  = 0
        flags     = 
        window    = 
        chksum    = 
        urgptr    = 0
        options   = []
###[ HTTP 1 ]### 
###[ HTTP Request ]### 
           Method    = 'POST'
           Path      = '/'
           Http_Version= 'HTTP/1.1'
           A_IM      = None
           Accept    = '*/*'
           Accept_Charset= None
           Accept_Datetime= None
           Accept_Encoding= 'gzip, deflate'
           Accept_Language= ''
           Access_Control_Request_Headers= None
           Access_Control_Request_Method= None
           Authorization= None
           Cache_Control= 'no-cache'
           Connection= 'keep-alive'
           Content_Length= '84'
           Content_MD5= None
           Content_Type= ''
           Cookie    = None
           DNT       = None
           Date      = None
           Expect    = None
           Forwarded = None
           From      = None
           Front_End_Https= None
           HTTP2_Settings= None
           Host      = ''
           If_Match  = None
           If_Modified_Since= None
           If_None_Match= None
           If_Range  = None
           If_Unmodified_Since= None
           Keep_Alive= None
           Max_Forwards= None
           Origin    = None
           Permanent = None
           Pragma    = 'no-cache'
           Proxy_Authorization= None
           Proxy_Connection= None
           Range     = None
           Referer   = None
           Save_Data = None
           TE        = None
           Upgrade   = None
           Upgrade_Insecure_Requests= None
           User_Agent= ''
           Via       = None
           Warning   = None
           X_ATT_DeviceId= None
           X_Correlation_ID= None
           X_Csrf_Token= None
           X_Forwarded_For= None
           X_Forwarded_Host= None
           X_Forwarded_Proto= None
           X_Http_Method_Override= None
           X_Request_ID= None
           X_Requested_With= None
           X_UIDH    = None
           X_Wap_Profile= None
           Unknown_Headers= None
###[ Raw ]### 
              load      = ''

```




### Features
***
- [ ] Nothing at this moment



### Contributing
***
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
