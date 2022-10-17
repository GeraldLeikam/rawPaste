# rawPaste

## Usage

<!-- Badges --> 
[![Website rawpaste.drezael.de](https://img.shields.io/website?down_color=red&down_message=down&style=plastic&up_color=green&up_message=up&url=http%3A%2F%2Frawpaste.drezael.de)](http://rawpaste.drezael.de)

Self-explanatory live examples (using public server):

```
echo Hello World! | nc rawpaste.drezael.de 9999
```

```
cat file.txt | nc rawpaste.drezael.de 9999
```

-------------------------------------------------------------------------------

## Installation

1. Install Prerequisites

   ```
   Ubunut/Debian:
   
   apt install -y python3 python3-pip 
   pip3 install pygments
   ```


3. Clone:

    ```
    git clone https://github.com/GeraldLeikam/rawPaste.git
    ```

4. Edit Config:

    ```
    nano ./rawPaste/config/config.yaml
    
    Change Server->Address from 127.0.0.1 (if you don't want to run it local) 
    to your IP address or domain e.g. your-domain.com or sub.your-domain.com
    ```
    
5. Run:

    ```
    cd ./rawPaste
    python3 main.py
    ```

-------------------------------------------------------------------------------