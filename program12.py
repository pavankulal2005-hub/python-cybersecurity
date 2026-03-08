#program 12
#check for security headers in a website
import requests
url = input("Enter URL: ")#http://testphp.vulnweb.com
r = requests.get(url)
headers = ["X-Frame-Options", "Content-Security-Policy","Strict-Transport-Security"]
for h in headers:
   if h in r.headers:
     print(h, "-> Present")
   else:
     print(h, "-> Missing (Potential Risk)")