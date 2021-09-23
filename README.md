# demo-sip

## Overview
A Python tool that loads a dump of SIP telephony registrations and then starts listening on a TCP socket for user input 
(a search for an Address of Record aka AOR either returns a JSON payload with more details from the dump file or an empty line if not found).

## How to use

**<span style="color:orange"><u>Pre-requisite:</u></span>** Python 3 _(tested with Python 3.9.7 on macOS Big Sur)_

1. Clone this repo then navigate to its root
2. Start the server script by running the following in a terminal session:
   
   ```shell
   python3 main.py
   ```

3. Now in a different terminal session we'll use netcat (client) to run a few search tests:
   
### **Test with no data**
```shell
echo -n | nc localhost 9999
```

#### Output:
```shell
Empty request
```

### **Test with wrong AOR**
```shell
echo -n '0142e2fa3543cb32b' | nc localhost 9999
```

#### Output:
```shell

```
    
### **Test with correct AOR from list**
```shell
echo -n 01546f59a9033db700000100610001 | nc localhost 9999
```

#### Output w/o jq:
```json
{"addressOfRecord": "01546f59a9033db700000100610001", "tenantId": "0127d974-f9f3-0704-2dee-000100420001", "uri": "sip:01546f59a9033db700000100610001@0.126.229.77:10902", "contact": "<sip:01546f59a9033db700000100610001@43.82.170.192:10902>;+sip.instance=\"<urn:uuid:58B7D3C8-145E-00EC-5FC2-861E57FD7FB2>\"", "path": ["<sip:Mi0xNzQuMTM0LjE0Ni4xODktMTA5MDI@200.59.12.96:5060;lr>"], "source": "238.116.236.172:10902", "target": "34.92.40.2:5061", "userAgent": null, "rawUserAgent": "Jive iOS Client", "created": "2017-01-06T13:25:25.539Z", "lineId": "01464e4a-6568-854b-fc96-000100620002"}
```

or _(requires jq to be installed)_

```shell
echo -n 01546f59a9033db700000100610001 | nc localhost 9999 | jq .
```  

#### Output with jq:
```json
{
  "addressOfRecord": "01546f59a9033db700000100610001",
  "tenantId": "0127d974-f9f3-0704-2dee-000100420001",
  "uri": "sip:01546f59a9033db700000100610001@0.126.229.77:10902",
  "contact": "<sip:01546f59a9033db700000100610001@43.82.170.192:10902>;+sip.instance=\"<urn:uuid:58B7D3C8-145E-00EC-5FC2-861E57FD7FB2>\"",
  "path": [
    "<sip:Mi0xNzQuMTM0LjE0Ni4xODktMTA5MDI@200.59.12.96:5060;lr>"
  ],
  "source": "238.116.236.172:10902",
  "target": "34.92.40.2:5061",
  "userAgent": null,
  "rawUserAgent": "Jive iOS Client",
  "created": "2017-01-06T13:25:25.539Z",
  "lineId": "01464e4a-6568-854b-fc96-000100620002"
}
```

### **Test with correct AOR from list but with added delay > 10 sec to trigger a timeout**

**<span style="color:red"><u>Note:</u> After running this command the socket will close, to re-open it run the command from Step 2**

```shell
echo -n 01546f59a9033db700000100610001 | nc localhost 9999 -i 11
```  

#### Output:
```shell

```