#pyshorteners module
import pyshorteners
shorteners = pyshorteners.Shortener()
long_link=input("your link : ")
short_link = shorteners.tinyurl.short(long_link)
print(short_link)