from requests import get
from assist import Doppelgang
def banner():
    banner = """\033[92;1m
    ██████   ██████  ██████  ██████  ███████ ██       ██████   █████  ███    ██  ██████  ███████ ██████  
    ██   ██ ██  ████ ██   ██ ██   ██ ██      ██      ██       ██   ██ ████   ██ ██       ██      ██   ██ 
    ██   ██ ██ ██ ██ ██████  ██████  █████   ██      ██   ███ ███████ ██ ██  ██ ██   ███ █████   ██████  
    ██   ██ ████  ██ ██      ██      ██      ██      ██    ██ ██   ██ ██  ██ ██ ██    ██ ██      ██   ██ 
    ██████   ██████  ██      ██      ███████ ███████  ██████  ██   ██ ██   ████  ██████  ███████ ██   ██ 

                                                                               by itsmmdoha aka HoundSec                                                                                                    
    \033[0m"""
    print(banner)
banner()

try:
    get("https://google.com")
except:
    exit("\033[91;1mGet an internet connection first; you moron!!!\033[0m \n")

url = input("\033[93mEnter the url to be masked: ")
mask = input("Enter a masking domain: ")
keyword = input("Type a kewword (without whitespace or / ): ")
target = Doppelgang(url,mask,keyword)
target.shorten()
print("Output url: \033[91;1m",target.mask(),"\033[0m")
