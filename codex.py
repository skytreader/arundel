import http.client
import urllib.parse

conn = http.client.HTTPConnection("0.0.0.0", 8000)
conn.request("GET", url="/")
print(conn.getresponse())
#conn.request("POST", url="/_index?filename=test.py", body="print('Hello world')")
conn.request("POST", "/_index", urllib.parse.urlencode({"filename": "test.py"}))
print(conn.getresponse())
