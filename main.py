from requests import get
from assist import Doppelgang

url = input("\033[93mEnter the url to be masked: ")
mask = input("Enter a masking domain: ")
keyword = input("Type a kewword (without whitespace or / ): ")
target = Doppelgang(url,mask,keyword)
target.shorten()
print("Output url: \033[91;1m",target.mask(),"\033[0m")
