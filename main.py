from requests import get
from json import loads

class Doppelgang:
    def __init__(self,url,maskingDomain="google.com",keyword="login"):
        self.url = url
        self.maskingDomain = maskingDomain
        self.keyword = keyword
        self.shorturl = None
    def shorten(self):
        res = get(f"https://is.gd/create.php?format=json&url={self.url}").text
        json = loads(res)
        self.shorturl = json["shorturl"]
        return self.shorturl

    def mask(self):
        maskedURL = self.shorturl.replace("https://",f"https://{self.maskingDomain}-{self.keyword}@")
        return maskedURL


if __name__ == "__main__":
    url = input("Enter the url to be masked: ")
    mask = input("Enter a masking domain: ")
    keyword = input("Type a kewword (without whitespace or / ): ")
    target = Doppelgang(url,mask,keyword)
    target.shorten()
    print("Output url:",target.mask())
