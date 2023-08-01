from requests import get
from requests.utils import quote as urlEncode
from json import loads

class Doppelgang:
    def __init__(self,url,maskingDomain="google.com",keyword="login"):
        self.url = url
        self.maskingDomain = maskingDomain
        self.keyword = keyword
        self.shorturl = None
    def shorten(self):
        encodedUrl = urlEncode(self.url)
        res = get(f"https://is.gd/create.php?format=json&url={encodedUrl}").text
        json = loads(res)
        self.shorturl = json["shorturl"]
        return self.shorturl

    def mask(self):
        maskedURL = self.shorturl.replace("https://",f"https://{self.maskingDomain}-{self.keyword}@")
        return maskedURL

