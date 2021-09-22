# demo-sip

### Work in progress, cleaner readme to follow

Use with Python 3 (pre-requisite)

1. Clone this repo then go to dir

2. Open in one terminal:
   
   `$ python3 main.py`

4. Open in another terminal:
  - **Test with no data**\
    `$ echo -n | nc localhost 9999`

  - **Test with wrong AOR**\
    `$ echo -n '0142e2fa3543cb32b' | nc localhost 9999`

  - **Test with correct AOR from list**\
    `$ echo -n 01546f59a9033db700000100610001 | nc localhost 9999`\
    or\
    `$ echo -n 01546f59a9033db700000100610001 | nc localhost 9999 | jq .`

### TODO:
- 10 sec timeout