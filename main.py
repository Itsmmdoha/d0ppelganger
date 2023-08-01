from assist import Doppelgang
url = input("Enter the url to be masked: ")
mask = input("Enter a masking domain: ")
keyword = input("Type a kewword (without whitespace or / ): ")
target = Doppelgang(url,mask,keyword)
target.shorten()
print("Output url:",target.mask())
